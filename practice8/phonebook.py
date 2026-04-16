from connect import get_connection
def _print_rows(rows):
    if not rows:
        print("  (no results)")
        return
    print(f"\n  {'ID':<5} {'First name':<15} {'Last name':<15} {'Phone':<20}")
    print("  " + "─" * 57)
    for r in rows:
        print(f"  {r[0]:<5} {r[1]:<15} {(r[2] or ''):<15} {r[3]:<20}")
    print()


def search_by_pattern():
    pattern = input("Enter search pattern (part of name or phone): ").strip()
    conn = get_connection()
    try:
        with conn.cursor() as cur:
            # search_by_pattern PostgreSQL функциясын қолданады
            cur.execute("SELECT * FROM search_by_pattern(%s)", (pattern,))
            _print_rows(cur.fetchall())
    finally:
        conn.close()

def upsert_one():
    firstname = input("First name : ").strip()
    lastname  = input("Last name  : ").strip()
    phone     = input("Phone      : ").strip()

    if not firstname or not phone:
        print("[ERROR] First name and phone are required.")
        return

    conn = get_connection()
    try:
        with conn.cursor() as cur:
            # upsert_contact PostgreSQL функциясын шақыру
            cur.execute("SELECT upsert_contact(%s, %s, %s)", (firstname, lastname or None, phone))
            conn.commit()
        print("[OK] Contact saved (inserted or updated).")
    except Exception as e:
        print(f"[ERROR] {e}")
        conn.rollback()
    finally:
        conn.close()

def bulk_insert():
    print("Enter contacts one by one. Leave first name blank to stop.")
    contacts = []
    
    while True:
        firstname = input("  First name (blank to finish): ").strip()
        if not firstname:
            break
        
        lastname = input("  Last name : ").strip()
        phone = input("  Phone     : ").strip()
        
        # Валидация
        if not firstname or not phone:
            print(f"  [WARN] First name and phone are required")
            continue
        if not phone.isdigit() or len(phone) < 10:
            print(f"  [WARN] Invalid phone format: {phone}")
            continue
        
        contacts.append({
            'firstname': firstname,
            'lastname': lastname if lastname else None,
            'phone': phone
        })
    
    if not contacts:
        print("[INFO] Nothing to insert.")
        return
    
    conn = get_connection()
    try:
        with conn.cursor() as cur:
            success_count = 0
            
            for contact in contacts:
                try:
                    # search_by_pattern арқылы телефон бар ма тексереміз
                    cur.execute("SELECT * FROM search_by_pattern(%s)", (contact['phone'],))
                    existing = cur.fetchall()
                    
                    if existing:
                        # Бар контактіні жаңарту үшін алдымен жоямыз сосын қосамыз
                        for old in existing:
                            # Жою үшін ID қолданамыз
                            cur.execute("SELECT delete_contact_by_id(%s)", (old[0],))
                        
                        # Жаңасын қосу
                        cur.execute("SELECT upsert_contact(%s, %s, %s)", 
                                  (contact['firstname'], contact['lastname'], contact['phone']))
                        print(f"  ✅ {contact['firstname']} {contact['lastname'] or ''} | {contact['phone']} - updated")
                    else:
                        # Жаңа контакт қосу
                        cur.execute("SELECT upsert_contact(%s, %s, %s)", 
                                  (contact['firstname'], contact['lastname'], contact['phone']))
                        print(f"  ✅ {contact['firstname']} {contact['lastname'] or ''} | {contact['phone']} - inserted")
                    
                    success_count += 1
                    conn.commit()
                    
                except Exception as e:
                    print(f"  ❌ {contact['firstname']} | {contact['phone']} - error: {e}")
                    conn.rollback()
            
            print(f"\n[OK] {success_count} contact(s) processed successfully.")
            
    except Exception as e:
        print(f"\n[ERROR] {e}")
        conn.rollback()
    finally:
        conn.close()

def paginated_query():
    try:
        limit = int(input("Rows per page [5]: ").strip() or "5")
        page = int(input("Page number  [1]: ").strip() or "1")
    except ValueError:
        print("[ERROR] Please enter valid numbers.")
        return

    offset = (page - 1) * limit
    conn = get_connection()
    try:
        with conn.cursor() as cur:
            # get_contacts_paginated PostgreSQL функциясын шақыру
            cur.execute("SELECT * FROM get_contacts_paginated(%s, %s)", (limit, offset))
            rows = cur.fetchall()
        print(f"\n  Page {page} (limit={limit}, offset={offset})")
        _print_rows(rows)
    finally:
        conn.close()

def delete_contact():
    print("Delete by:")
    print("  1. Name")
    print("  2. Phone")
    choice = input("Choice (1/2): ").strip()
    
    conn = get_connection()
    try:
        with conn.cursor() as cur:
            if choice == '1':
                name = input("First name to delete: ").strip()
                confirm = input(f"Delete all contacts with name '{name}'? (y/n): ").strip().lower()
                if confirm == 'y':
                    # Бірінші іздеу арқылы контактілерді табу
                    cur.execute("SELECT * FROM search_by_pattern(%s)", (name,))
                    to_delete = cur.fetchall()
                    
                    if to_delete:
                        # Әр контактіні ID бойынша жою
                        for contact in to_delete:
                            try:
                                cur.execute("DELETE FROM phonebook WHERE id = %s", (contact[0],))
                            except:
                                # Егер тікелей DELETE жұмыс істемесе, басқа функция қолдану
                                cur.execute("SELECT delete_contact_by_id(%s)", (contact[0],))
                        conn.commit()
                        print(f"\n✅ Deleted {len(to_delete)} contact(s):")
                        for contact in to_delete:
                            print(f"   - {contact[1]} {contact[2] or ''} | {contact[3]}")
                    else:
                        print(f"\n❌ No contacts found with name '{name}'")
            
            elif choice == '2':
                phone = input("Phone number to delete: ").strip()
                confirm = input(f"Delete contact with phone '{phone}'? (y/n): ").strip().lower()
                if confirm == 'y':
                    cur.execute("SELECT * FROM search_by_pattern(%s)", (phone,))
                    to_delete = cur.fetchall()
                    
                    if to_delete:
                        for contact in to_delete:
                            try:
                                cur.execute("DELETE FROM phonebook WHERE id = %s", (contact[0],))
                            except:
                                cur.execute("SELECT delete_contact_by_id(%s)", (contact[0],))
                        conn.commit()
                        print(f"\n✅ Deleted {len(to_delete)} contact(s):")
                        for contact in to_delete:
                            print(f"   - {contact[1]} {contact[2] or ''} | {contact[3]}")
                    else:
                        print(f"\n❌ No contacts found with phone '{phone}'")
    except Exception as e:
        print(f"\n❌ Error: {e}")
        conn.rollback()
    finally:
        conn.close()


def menu():
    while True:
        print("\n═══════════ PhoneBook – Practice 8 ═══════════")
        print(" 1. Search contacts by pattern")
        print(" 2. Add / update one contact  (upsert)")
        print(" 3. Bulk insert contacts with validation")
        print(" 4. Browse contacts (paginated)")
        print(" 5. Delete a contact")
        print(" 0. Exit")
        print("═══════════════════════════════════════════════")
        choice = input("Choose: ").strip()

        if   choice == "1": search_by_pattern()
        elif choice == "2": upsert_one()
        elif choice == "3": bulk_insert()
        elif choice == "4": paginated_query()
        elif choice == "5": delete_contact()
        elif choice == "0":
            print("Bye!")
            break
        else:
            print("[ERROR] Unknown option.")


if __name__ == "__main__":
    menu()
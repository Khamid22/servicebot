import asyncio

from utils.db_api.db_commands import Database


async def test():
    db = Database()
    await db.create()

#     print("Creating the table of users...")
#     await db.drop_users()
#     await db.create_table_users()
#     print("Created")
#
#     print("Adding new user")
#
#     await db.add_user("anvar", "sariqdev", 123456789)
#     await db.add_user("olim", "olim223", 12341123)
#     await db.add_user("1", "1", 131231)
#     await db.add_user("1", "1", 23324234)
#     await db.add_user("John", "JohnDoe", 4388229)
#     print("Joined")
#
#     users = await db.select_all_users()
#     print(f"All users: {users}")
#
#     user = await db.select_user(id=5)
#     print(f"User: {user}")
#
#

    print("Creating table of customers...")
    await db.create_table_customers()
    print("Created")
    await db.add_customer("Khamidullo", "+998905411173", "BMW", "tuning", "Monday 9:50-13:00")
    print("Joined")

    customers = await db.sel
import psycopg2

conn = psycopg2.connect(
    host="40.69.141.190",
    database="sw-cloud",
    user="postgres",
    password="7XH0DH7qaMDdRRddgyU0zmCo",
    port=5432
)

cur = conn.cursor()
result = cur.execute(
    'select u.id, "phoneNumber", otp from "Users" u left join public."UserValidation" uv on u.id = uv."userId"  where u."phoneNumber" = \'+917030095990\'')
otp = cur.fetchone()
print(otp[2])

conn.close()

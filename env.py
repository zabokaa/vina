import os

os.environ.setdefault(
    "DATABASE_URL", 
    "postgresql://vinadb_owner:PG5BoeTqkpj9@ep-billowing-dawn-a5a2zh5m.us-east-2.aws.neon.tech/vinadb?sslmode=require"
    )
os.environ.setdefault("SECRET_KEY", "u#x$^C4pxz6sqVNs^M8DuQRHDM7!fz")
os.environ.setdefault("CLOUDINARY_URL", "cloudinary://557819564883823:Jv5NTKghKCyv5vKP1QpPpgAqln0@dszgdroxd")

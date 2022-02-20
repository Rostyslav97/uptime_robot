from config.settings.base import env

DATABASES = {
    "default": env.db_url(
        "DATABASE_URL",
        default="postgres://postgres:postgres@postgres:7000/uptime_robot",
    )
}
from aiogram import Router

from .admin import router as admin
from .start import router as start


router = Router()


router.include_routers(start, admin)
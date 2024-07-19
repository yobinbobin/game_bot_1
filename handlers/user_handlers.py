from aiogram import F, Router
from aiogram.filters import Command, CommandStart
from aiogram.types import Message
from keyboards.keyboars import game_kb, yes_no_kb
from lexicon.lexicon import lexicon_ru
from services.services import get_bot_choice, get_winner

router = Router()

@router.message(CommandStart())
async def start_command(message: Message):
    await message.answer(text = lexicon_ru['/start'],
                         reply_markup=yes_no_kb)


@router.message(Command(commands='help'))
async def process_help_command(message: Message):
    await message.answer(text=lexicon_ru['/help'], reply_markup=yes_no_kb)


@router.message(F.text == lexicon_ru['yes_button'])
async def process_yes_answer(message: Message):
    await message.answer(text=lexicon_ru['yes'], reply_markup=game_kb)


@router.message(F.text == lexicon_ru['no_button'])
async def process_no_answer(message: Message):
    await message.answer(text=lexicon_ru['no'])


@router.message(F.text.in_([lexicon_ru['rock'],
                            lexicon_ru['paper'],
                            lexicon_ru['scissors']]))
async def process_game_button(message: Message):
    bot_choice = get_bot_choice()
    await message.answer(text=f'{lexicon_ru["bot_choice"]} '
                              f'- {lexicon_ru[bot_choice]}')
    winner = get_winner(message.text, bot_choice)
    await message.answer(text=lexicon_ru[winner], reply_markup=yes_no_kb)
import logging
import requests

from aiogram import Bot, Dispatcher, types
from aiogram.utils import executor
from aiogram.utils.markdown import text, bold, italic

API_TOKEN = '5804466387:AAHZuCRiLGaflm-heNuWy8zFE-egHxmrIpE'

# For example use simple console logging
logging.basicConfig(level=logging.INFO)

# Initialize bot and dispatcher
bot = Bot(token=API_TOKEN)
dp = Dispatcher(bot)

import requests

# Replace YOUR_API_KEY with your actual API key
API_KEY = 'YOUR_API_KEY'

def get_air_quality(location):
    # Make a GET request to the Open AQ API to retrieve air quality data for the given location
    url = f'https://api.openaq.org/v1/latest?country={location}'
    headers = {'Authorization': f'Bearer {API_KEY}'}
    response = requests.get(url, headers=headers)
    
    # Check if the request was successful
    if response.status_code == 200:
        # Parse the response data
        data = response.json()
        return data
    else:
        # There was an error making the request
        return None


# Command /start
@dp.message_handler(commands='start')
async def cmd_start(message: types.Message):
    """
    Conversation's entry point
    """
    # Set state
    await bot.send_message(
        message.chat.id,
        "Salom! Men atrof-muhitni qanday saqlash haqida ma'lumot beruvchi botman.\n"
         "Mavjud buyruqlar roʻyxatini koʻrish uchun /help ni kiriting."
    )

# Command /help
@dp.message_handler(commands='help')
async def cmd_help(message: types.Message):
    """
    the command /help 
    """
    await bot.send_message(
        message.chat.id,
        "Bu erda mavjud buyruqlar ro'yxati:\n"
        " - /start: Botni ishga tushiring va salomlashish xabarini oling\n"
        " - /about: Bot haqida ma'lumot oling\n"
        " - /ecology: Ekologiyaning ahamiyati haqida bilib oling\n"
        " - /how_to_save_environment: Atrof-muhitni qanday saqlash bo'yicha maslahatlar oling\n"
        " - /social_media: Bizning sotsial tarmoqlarimizni olishing\n "
        " - /green_uzbekistan O'zbekistonni yashil davlatga aylantiramiz\n "
        # " - /air_pollution_level"
        " - /donate: Bizga yordam bering va O'zbekistonni yashil davlatga aylantirishga qo'shiling\n" 
        
    )

# Command /about
@dp.message_handler(commands='about')
async def cmd_about(message: types.Message):
    """
    the command /about 
    """
    await bot.send_message(
        message.chat.id,
        "Men atrof-muhitni qanday saqlash haqida ma'lumot berish uchun ishlab chiqilgan botman. "
        "Mening vazifam O'zbekistonda ekalogiyani yaxshilash. Va Yashil hududlarni ko'paytirishdir "
    )

# Command /ecology
@dp.message_handler(commands='ecology')
async def cmd_ecology(message: types.Message):
    """
    the command /ecology 
    """
    await bot.send_message(
        message.chat.id,
        "Ekologiya - bu organizmlar va ularning atrof-muhit o'rtasidagi munosabatlarni o'rganadigan fan. Bu muhim soha\n "
        "chunki bu bizga tirik mavjudotlarning bir-biri bilan va ularning atrofi bilan qanday munosabatda bo'lishini va qanday qilib tushunishga yordam beradi \n"
        "inson harakatlari tabiiy dunyoga ta'sir qilishi mumkin. Ekologiyani tushunish bizga tegishli qarorlar qabul qilishga yordam beradi\n"
        "tabiiy resurslardan barqaror foydalanish va atrof-muhitni muhofaza qilish."
    )

# Command /how_to_save_environment
@dp.message_handler(commands='how_to_save_environment')
async def cmd_how_to_save_environment(message: types.Message):
    """
    Send a message when the command
    """

    await bot.send_message(
        message.chat.id,
        "1: Energiyani tejaydigan asboblardan foydalanish, avtomashinalar yoki jamoat transportidan foydalanish va umumiy energiya sarfini kamaytirish orqali uglerod izingizni kamaytiring.\n"
        "2: Chiqindilarni va yangi materiallarga bo'lgan talabni kamaytirish uchun iloji boricha qayta ishlang va kompost qiling.\n"
        "3: Qayta tiklanadigan energiya va tabiatni muhofaza qilish kabi ekologik toza amaliyotlarni targ‘ib qiluvchi tashkilotlar va siyosatlarni qo‘llab-quvvatlash.\n"
        "4: Atmosferadan karbonat angidridni o'zlashtiradigan va iqlim o'zgarishiga qarshi kurashda yordam beradigan daraxtlar va boshqa o'simliklar eking.\n"
        "5: Bir marta ishlatiladigan narsalardan chiqindilarni kamaytirish uchun qayta ishlatiladigan sumkalar, idishlar va suv idishlaridan foydalaning.\n"
        "6: Mahalliy qishloq xo'jaligini qo'llab-quvvatlang va iloji bo'lsa, ekologik toza mahsulotlarni tanlang.\n"
        "7: O'zingizni va boshqalarni atrof-muhit muammolari va sayyorani qanday himoya qilish haqida ma'lumot bering.\n"
        "Yoki bizning hisobga pul o'tkazib beradigan bo'lsangiz biz daraxtlarni ekish bo'yicha shug'ullanadigan fondga pullarni o'tkazamiz."
    )

# Command /social_media
@dp.message_handler(commands='social_media')
async def cmd_social_media(message: types.Message):
    """
    Send a message when the command /social_media is issued.
    """
    social_media_text = (
        f"You can find us on the following social media platforms:\n"
        f"{bold('Twitter')}: https://twitter.com/\n"
        f"{bold('Facebook')}: https://facebook.com\n"
        f"{bold('Instagram')}: https://instagram.com\n"
        f"{bold('Bizning veb-sayt')}: https://google.com" # o'zuzani saytti linkini qo'yish kere
    )
    await bot.send_message(message.chat.id, social_media_text, parse_mode=types.ParseMode.MARKDOWN)

# Command /green_uzbekistan
@dp.message_handler(commands='green_uzbekistan')
async def cmd_green_uzbekistan(message: types.Message):
    """
    Send a message when the command /green_uzbekistan is issued.
    """
    green_uzbekistan_text = (
        "Qanday qilib O'zbekistonda yashil xudularni ko'paytirish mumkin\n" 
        "1: Daraxtlar va boshqa o'simliklarni ekish: Bu parklar va ko'chalar bo'ylab jamoat joylarida, shuningdek, xususiy mulkda amalga oshirilishi mumkin.\n"
        "2: Jamoa bog'larini yaratish: Bular odamlarga o'z oziq-ovqatlarini etishtirishga imkon beradi va bo'sh joylarda yoki boshqa to'liq foydalanilmaydigan joylarda joylashgan bo'lishi mumkin.\n"
        "3: Yashil infratuzilmadan foydalanishni rag'batlantirish: Bu suv o'tkazuvchan yo'laklar, yomg'ir bog'lari va boshqa turdagi landshaft xususiyatlarini o'z ichiga olishi mumkin, ular bo'ron suvi oqimini boshqarishga va hududdagi suv o'tkazmaydigan sirtlar miqdorini kamaytirishga yordam beradi.\n"
        "4: Yashil maydonni himoya qilish uchun mahalliy hukumatlar va jamoat tashkilotlari bilan ishlash: Bu ko'kalamzorlashtirish loyihalarini moliyalashtirish uchun lobbichilikni, yashil maydonlarga ustuvorlik berish uchun rayonlashtirish qonunlarini yoki rivojlanish rejalarini o'zgartirish ustida ishlashni yoki jamoat joylarini tozalash va ko'kalamzorlashtirish tadbirlarini tashkil etishni o'z ichiga olishi mumkin."
    )
    await bot.send_message(message.chat.id, green_uzbekistan_text)

# Command /donate
@dp.message_handler(commands='donate')
async def cmd_donate(message: types.Message):
    """
     the command /donate
    """
    donate_text = (
        "Bizni qo'llab quvatlaganingiz uchun raxmat."
        f"{bold('Donate')}: https://www.donationalerts.com/r/green_uzbekistan"
    )
    await bot.send_message(message.chat.id, donate_text)

API_KEY = 'bca9e5ae-6a99-4523-9b60-0db18323e7a6'

def get_air_pollution_level(location):
    url = f'http://api.airvisual.com/v2/city?city={location}&state=&country=Uzbekistan&key={API_KEY}'
    response = requests.get(url)
    
    # Check if the request was successful
    if response.status_code == 200:
        # Parse the response data
        data = response.json()
        # Get the air pollution level from the data
        air_pollution_level = data['data']['current']['pollution']['aqius']
        return air_pollution_level
    else:
        # There was an error making the request
        return None

# Example usage
location = 'Tashkent'
air_pollution_level = get_air_pollution_level(location)

if air_pollution_level is not None:
    print(f'The air pollution level in {location} is {air_pollution_level}')
else:
    print(f'Unable to retrieve air pollution level for {location}')

# Command /air_pollution_level
@dp.message_handler(commands='air_pollution_level')
async def cmd_air_pollution_level(message: types.Message):
    # Split the message text into a list of arguments
    args = message.text.split()

    # Check if a location was provided
    if len(args) < 2:
        await bot.send_message(
            message.chat.id,
            "Iltimos, havoning ifloslanish darajasini olmoqchi bo'lgan joyni belgilang.\n"
            "Misol: '/air_pollution_level New York'"
        )
        return

    # Get the location from the message arguments
    location = args[1]

    # Get the air quality data for the location
    data = get_air_quality(location)
    
    if data is None:
        # There was an error making the request
        await bot.send_message(
            message.chat.id,
            "Sorry, there was an error getting the air pollution data for the specified location. Please try again later."
        )
        return

    # Get the average air pollution level for the location
    pollution_level = data['results'][0]['average']['pm25']

    # Send a message with the air pollution level to the user
    await bot.send_message(
        message.chat.id,
        f"The air pollution level in {location} is {pollution_level}."
    )

if __name__ == '__main__':
    executor.start_polling(dp)
    
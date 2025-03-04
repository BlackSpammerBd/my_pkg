from setuptools import setup, find_packages

setup(
    name="BlackSpammerBd_bot",
    version="1.0",
    packages=find_packages(),
    install_requires=[
        "telebot",  # টেলিগ্রাম API
        "watchdog",  # ফাইল মনিটরিং
        "android-helper",  # অ্যান্ড্রয়েডের SMS, কন্টাক্ট, ফাইল এক্সেস করার জন্য
    ],
    entry_points={
        "console_scripts": [
            "bsb = BlackSpammerBd_bot.main:main",
        ],
    },
)

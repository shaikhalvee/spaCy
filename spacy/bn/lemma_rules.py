# encoding: utf8
from __future__ import unicode_literals

# Source: উচ্চতর বাংলা ব্যকরণ ও রচনা (অধ্যাপক নিরঞ্জন অধিকারী ও অধ্যাপক ড. সফিউদ্দিন আহমদ) - Grammar Book

LEMMA_RULES = {
    "noun": [
        # suffixes for indicating singular
        ["টি", ""],  # ti
        ["টা", ""],  # ta
        ["খান", ""],  # khan
        ["খানা", ""],  # khana
        ["খানি", ""],  # khani
        ["গাছা", ""],  # gacha
        ["গাছি", ""],  # gachi
        ["ছড়া", ""],  # chora

        # suffixes for indicating plural
        ["রা", ""],  # ra
        ["েরা", ""],  # era
        ["গুলো", ""],  # gulo
        ["দের", ""],  # der
        ["গুলা", ""],  # gula
        ["গুলো", ""],  # gulo
        ["গুলি", ""],  # guli
        ["দের", ""],  # der
        ["সমূহ", ""],  # somuho
        ["কুল", ""],  # kul
        ["গণ", ""],  # gon
        ["দল", ""],  # dol
        ["পাল", ""],  # pal
        ["পুঞ্জ", ""],  # punjo
        ["মণ্ডলী", ""],  # mondoli
        ["মালা", ""],  # mala
        ["রাজি", ""],  # raji
        ["বৃন্দ", ""],  # brindo
        ["বর্গ", ""],  # borgo
        ["শ্রেণি", ""],  # shreni
        ["শ্রেণী", ""],  # shreni (emphasis on I)
        ["সব", ""],  # shob
        ["রাশি", ""],  # rashi
        ["সকল", ""],  # shokol
        ["মহল", ""],  # mohol
        ["াবলি", ""],  # aboli
    ],

    "verb": [],

    "adj": [],

    "punct": [
        ["“", "\""],
        ["”", "\""],
        ["\u2018", "'"],
        ["\u2019", "'"]
    ]
}

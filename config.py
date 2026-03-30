"""麻雀戦術ラボ - ブログ固有設定

牌効率・押し引き・読みを科学する。
データと理論で勝率を上げる麻雀戦術ブログ。
"""
import os
from pathlib import Path

BASE_DIR = Path(__file__).parent

BLOG_NAME = "麻雀戦術ラボ"
BLOG_DESCRIPTION = "牌効率・押し引き・読みを科学する。初心者から上級者まで、データと理論で勝率を上げる麻雀戦術ブログ"
BLOG_URL = "https://musclelove-777.github.io/mahjong-sensei"
BLOG_LANGUAGE = "ja"
GITHUB_REPO = "MuscleLove-777/mahjong-sensei"

# 記事カテゴリ
TARGET_CATEGORIES = [
    "牌効率・手組み",
    "押し引き判断",
    "副露戦術",
    "点数計算・符計算",
    "Mリーグ・プロ麻雀",
    "初心者講座",
    "データ分析・統計",
    "麻雀メンタル",
]

# テーマカラー（濃い緑系 - 麻雀卓をイメージ）
THEME = {
    "primary": "#1a5632",
    "accent": "#2d8a4e",
    "gradient_start": "#1a5632",
    "gradient_end": "#2d8a4e",
    "dark_bg": "#0a1a10",
    "dark_surface": "#112b1a",
    "light_bg": "#edf7f0",
    "light_surface": "#ffffff",
}

# 記事生成設定
MAX_ARTICLE_LENGTH = 3000
ARTICLES_PER_DAY = 3
SCHEDULE_HOURS = [7, 12, 19]

# Gemini API設定
GEMINI_API_KEY = os.environ.get("GEMINI_API_KEY", "")
GEMINI_MODEL = "gemini-2.5-flash"

# SEO最適化設定
ENABLE_SEO_OPTIMIZATION = True
MIN_SEO_SCORE = 70
MIN_KEYWORD_DENSITY = 1.0
MAX_KEYWORD_DENSITY = 3.0
META_DESCRIPTION_LENGTH = 120
ENABLE_INTERNAL_LINKS = True

# アフィリエイトリンク設定
AFFILIATE_LINKS = {
    "麻雀用品": [
        {
            "service": "Amazon 麻雀用品",
            "url": "https://www.amazon.co.jp/s?k=%E9%BA%BB%E9%9B%80+%E7%94%A8%E5%93%81",
            "description": "全自動卓・牌セット・マットなど麻雀グッズが豊富",
        },
        {
            "service": "楽天 麻雀用品",
            "url": "https://search.rakuten.co.jp/search/mall/%E9%BA%BB%E9%9B%80+%E7%94%A8%E5%93%81/",
            "description": "ポイント還元でお得に麻雀グッズを購入",
        },
    ],
    "麻雀アプリ": [
        {
            "service": "天鳳",
            "url": "https://tenhou.net/",
            "description": "日本最大級のオンライン麻雀。段位戦で実力を測定",
        },
        {
            "service": "雀魂(じゃんたま)",
            "url": "https://mahjongsoul.com/",
            "description": "美麗なキャラクターと対局が楽しめるオンライン麻雀",
        },
    ],
    "書籍": [
        {
            "service": "Amazon 麻雀本",
            "url": "https://www.amazon.co.jp/s?k=%E9%BA%BB%E9%9B%80+%E6%88%A6%E8%A1%93",
            "description": "麻雀戦術書・入門書・プロの著書が揃う",
        },
        {
            "service": "楽天ブックス 麻雀",
            "url": "https://books.rakuten.co.jp/search?sitem=%E9%BA%BB%E9%9B%80+%E6%88%A6%E8%A1%93",
            "description": "麻雀関連書籍をポイントで購入",
        },
    ],
    "オンライン麻雀": [
        {
            "service": "DORA麻雀",
            "url": "https://doramahjong.com/",
            "description": "リアルマネーで対局できるオンライン麻雀",
        },
    ],
}
AFFILIATE_TAG = "musclelove07-22"

# AdSense設定
ADSENSE_CLIENT_ID = os.environ.get("ADSENSE_CLIENT_ID", "")

# ダッシュボードポート
DASHBOARD_PORT = 8098

# Google Analytics (GA4)
GOOGLE_ANALYTICS_ID = "G-CSFVD34MKK"

# Google Search Console 認証ファイル
SITE_VERIFICATION_FILES = {
    "googlea31edabcec879415.html": "google-site-verification: googlea31edabcec879415.html",
}

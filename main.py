
from flask import Flask, request
import requests

app = Flask(__name__)

@app.route('/webhook', methods=['POST'])
def webhook():
    data = request.json
    print("== تم استقبال تنبيه من TradingView ==")
    print("المحتوى:", data)

    # تحليل وهمي لأزواج Binance (مثال فقط على BTCUSDT)
    symbol = "BTCUSDT"
    print(f"جاري فحص الزوج: {symbol}")

    # قراءة بيانات سعر وهمي وتنفيذ منطق استراتيجي بسيط
    # في نسخة حقيقية، يتم استخدام Binance API مباشرة
    close_prices = [50000, 50200, 50400, 50600, 50800, 51000, 51200, 51400, 51600]
    ema9 = sum(close_prices[-9:]) / 9
    ema21 = sum(close_prices[-9:] + [49800]*12) / 21

    if ema9 > ema21:
        print(f"جاهز شراء: {symbol} (EMA9 > EMA21)")

    return {"status": "success"}, 200

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)

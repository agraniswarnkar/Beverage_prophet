from django.shortcuts import render
from django.http import HttpResponse, Http404
import yfinance as yf 
import matplotlib.pyplot as plt


# Create your views here.
def index(request):
    return render(request, "singlepage/index.html")


'''texts = ["Lorem ipsum dolor sit amet, consectetur adipiscing elit. Aliquam tortor mauris, maximus semper volutpat vitae, varius placerat dui. Nunc consequat dictum est, at vestibulum est hendrerit at. Mauris suscipit neque ultrices nisl interdum accumsan. Sed euismod, ligula eget tristique semper, lecleo mi nec orci. Curabitur hendrerit, est in ",
        "Praesent euismod auctor quam, id congue tellus malesuada vitae. Ut sed lacinia quam. Sed vitae mattis metus, vel gravida ante. Praesent tincidunt nulla non sapien tincidunt, vitae semper diam faucibus. Nulla venenatis tincidunt efficitur. Integer justo nunc, egestas eget dignissim dignissim,  facilisis, dictum nunc ut, tincidunt diam.",
        "Morbi imperdiet nunc ac quam hendrerit faucibus. Morbi viverra justo est, ut bibendum lacus vehicula at. Fusce eget risus arcu. Quisque dictum porttitor nisl, eget condimentum leo mollis sed. Proin justo nisl, lacinia id erat in, suscipit ultrices nisi. Suspendisse placerat nulla at volutpat ultricies"]

def section(request, num):
    if 1 <= num <= 3:
        return HttpResponse(texts[num-1])
    else:
        raise Http404("No such section")'''


def service(request):
    return render(request, "singlepage/service.html")

def help(request):
    return render(request, "singlepage/help.html")

def about(request):
    return render(request, "singlepage/about.html")

def home(request):
    return render(request, "singlepage/home.html")

def datapresenting(request):
    return render(request, "singlepage/datapresenting.html")

def service_page(request):
    # Fetch data for AAPL, META, AMZN, GOOGL
    aapl_data = yf.download('AAPL', start='2023-01-01', end='2023-01-31')
    meta_data = yf.download('META', start='2023-01-01', end='2023-01-31')
    amzn_data = yf.download('AMZN', start='2023-01-01', end='2023-01-31')
    googl_data = yf.download('GOOGL', start='2023-01-01', end='2023-01-31')

    # Convert data to JSON format
    aapl_json = aapl_data.to_json()
    meta_json = meta_data.to_json()
    amzn_json = amzn_data.to_json()
    googl_json = googl_data.to_json()

    # Pass data to the template
    return render(request, 'singlepage/service.html', {'aapl_data': aapl_json, 'meta_data': meta_json, 'amzn_data': amzn_json, 'googl_data': googl_json})    

def data_presenting(request):
    msft_data = yf.download('MSFT', period='3mo')
    aapl_data = yf.download('AAPL', period='3mo') 
    msft_json = msft_data.to_json(orient='split')
    aapl_json = aapl_data.to_json(orient='split')  
    plt.figure(figsize=(10,6))
    plt.plot(msft_data['Close'], label='MSFT')
    plt.xlabel('Date')
    plt.ylabel('Closing Price')
    plt.title('MSFT Stock Price')
    plt.legend()
    plt.savefig('singlepage/static/images/msft_stock_price.png')
    plt.show()
    plt.close()

    # Plot AAPL data
    plt.plot(aapl_data['Close'], label='AAPL')
    plt.xlabel('Date')
    plt.ylabel('Closing Price')
    plt.title('AAPL Stock Price')
    plt.legend()
    plt.savefig('singlepage/static/images/aapl_stock_price.png')
    plt.show()
    plt.close()


    return render(request, 'datapresenting.html')
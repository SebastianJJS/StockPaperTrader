from django.core.management.base import BaseCommand
from stocks.models import Stock
from stocks.services import fetch_current_price

class Command(BaseCommand):
    help = 'Updates stock prices'

    def handle(self, *args, **kwargs):
        stocks = Stock.objects.all()
        if not stocks.exists():
            self.stdout.write(self.style.ERROR("No stocks found in the database."))
            return

        for stock in stocks:
            self.stdout.write(self.style.NOTICE(f"Fetching current price for {stock.symbol}..."))
            new_price = fetch_current_price(stock.symbol)
            if new_price:
                self.stdout.write(self.style.SUCCESS(f"Fetched current price for {stock.symbol}: {new_price}"))
                stock.current_price = new_price
                stock.save()
                self.stdout.write(self.style.SUCCESS(f"Updated {stock.symbol} to {stock.current_price}"))
            else:
                self.stdout.write(self.style.ERROR(f"Failed to fetch/update price for {stock.symbol}"))
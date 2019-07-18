import discord
import requests
import bs4

client = discord.Client()

@client.event
async def on_message(message):
    # we do not want the bot to reply to itself
    if message.author == client.user:
        return
    # Running commands list to help make use of bot easier
    commands_list = ['!help', '!commands']
    if any(command in message.content.lower() for command in commands_list):
        msg = 'Hello {0.author.mention}'.format(message)
        await client.send_message(message.channel, msg + ', currently the only commands that are active are !price "Insert Ticker Here" which will display the current price of a stock.')

    # Utilizing BeautifulSoup and Requests to web scrape price data from Yahoo.
    elif message.content.startswith('!price'):
        #Splitting the input from !price to read input text from user.
        stock = message.content.split(' ')[1]
        url = "https://finance.yahoo.com/quote/"

        full_url = url + stock

        response = requests.get(full_url).content

        soup = bs4.BeautifulSoup(response, 'html.parser')

        stock_price = soup.findAll(class_ = "Trsdu(0.3s) Trsdu(0.3s) Fw(b) Fz(36px) Mb(-4px) D(b)")[0].text

        await client.send_message(message.channel, f"The stock price for {stock.upper()} is ${stock_price} currently.")

@client.event
async def on_ready():
    print('Logged in as')
    print(client.user.name)
    print(client.user.id)
    print('------')

client.run('INSERT DISCORD TOKEN HERE - Found at https://discordapp.com/developers/applications/')

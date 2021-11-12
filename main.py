from discord.ext import commands, tasks
from selenium import webdriver
from selenium.common.exceptions import TimeoutException
import checkingOutProperly
import discord

#subsitute john with the name of the instance you created in checkingOutProperly

def read(driver, locator):
    driver.implicitly_wait(10)
    element = driver.find_element_by_xpath(locator).text
    return element


driver = webdriver.Chrome(executable_path=r"C:\Users\aalba\OneDrive\Desktop\chromedriver.exe")
client = commands.Bot(command_prefix="!")
count = 0

def checkCronusZen():
    try:
        driver.get("https://collectiveminds-uk.myshopify.com/products/cronus-zen")
        return read(driver, '//*[@id="AddToCart-product-template"]')
    except:
        return (str(TimeoutException))


@client.event
async def on_ready():
    print("Bot is ready")


@tasks.loop(seconds=30)
async def check_cronus_zen():

    x = checkCronusZen()
    if x != "SOLD OUT":
        global count
        count += 1
        channel = await client.fetch_channel("insert the channel you want the messages to be sent to here")

        await channel.send("CRONUS ZEN IS IN STOCK @everyone! I am buying them right now! https://collectiveminds-uk.myshopify.com/products/cronus-zen")
        await channel.send(checkingOutProperly.john.buy(1))


    elif x == "TimeoutException":
        channel = await client.fetch_channel("insert the channel you want the messages to be sent to here")
        await channel.send("Sorry, there has been an error. Please send the command again")


@client.command()
async def monitor(ctx, enabled="start"):
    if enabled.lower() == "stop":
        check_cronus_zen.cancel()
    elif enabled.lower() == "start":
        check_cronus_zen.start()


@client.command()
async def successful_order(ctx):
    nicely = discord.Embed(
        title='ORDER SUCCESSFUL',
        colour=discord.Colour.green()
    )
    channel = await client.fetch_channel("insert the channel you want the messages to be sent to here")
    nicely.set_thumbnail(url='https://cdn.shopify.com/s/files/1/0306/9558/7884/products/cronus_zen_trans_shadow_800_1024x1024.png?v=1588706228')
    nicely.add_field(name="Product Name", value="Cronus Zen", inline=False)
    nicely.add_field(name="Name", value=f"{checkingOutProperly.john.name_on_card}   ", inline=True)
    nicely.add_field(name="Email", value=checkingOutProperly.john.email, inline=True)
    #nicely.set_footer(text=date)


    await channel.send(embed=nicely)



@client.command()
async def failed_order(ctx):
    nicely = discord.Embed(
        title='ORDER SUCCESSFUL',
        colour=discord.Colour.green()
    )
    channel = await client.fetch_channel("insert the channel you want the messages to be sent to here")
    nicely.set_thumbnail(url='https://cdn.shopify.com/s/files/1/0306/9558/7884/products/cronus_zen_trans_shadow_800_1024x1024.png?v=1588706228')
    nicely.add_field(name="Product Name", value="Cronus Zen", inline=False)
    nicely.add_field(name="Name", value=f"{checkingOutProperly.john.name_on_card}   ", inline=True)
    nicely.add_field(name="Email", value=checkingOutProperly.john.email, inline=True)
    #nicely.set_footer(text=date)


    await channel.send(embed=nicely)


client.run("insert your discord application bot token here")

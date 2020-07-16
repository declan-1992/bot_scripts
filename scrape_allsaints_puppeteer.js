/* TO DO - Script currently only obtains the first item from the webpage --> need to include a loop to get all items from webpage */

//import puppeteer
const puppeteer = require('puppeteer');

(async () =>{

    //select target page
    let allsaints = 'https://www.allsaints.com/men/sale/coats-and-jackets/style,any/colour,any/size,any/'

    //start puppeteer with some options
    let browser = await puppeteer.launch({
        headless: false,
    });

    //launch a new puppeteer browser page
    let page = await browser.newPage();

    //go to allsaints website
    await page.goto(allsaints, {waitUntil: 'networkidle2'});

    //Let's puppeteer examine the HTML code of the page you are targeting 
    let scraped_data = await page.evaluate(() => {

        //Get item description from the HTML code --> <span class="product-item__name__text">
        let Description = document.querySelector('span[class="product-item__name__text"]').innerText.trim();

        //Get pre-sale price from the HTML code --> <span class="product-item__price-old">
        let Old_Price = document.querySelector('span[class="product-item__price-old"]').innerText.trim();

        //Get sale price from the HTML code --> <span class="product-item__price-new">
        let New_Price = document.querySelector('span[class="product-item__price-new"]').innerText.trim();

        //Return scraped info
        return{
            Description,
            Old_Price,
            New_Price
        }


    });

    //show info in terminal
    console.log(scraped_data);
    
    //close browser
    await browser.close();

})();

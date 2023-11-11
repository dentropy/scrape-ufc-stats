import puppeteer from 'puppeteer';

function sleep(seconds) {
    const milliseconds = seconds * 1000;
    return new Promise(resolve => setTimeout(resolve, milliseconds));
  }

(async () => {
  // Launch the browser and open a new blank page
  const browser = await puppeteer.launch({
    headless: false
  });
  const page = await browser.newPage();
  await page.setUserAgent('Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/77.0.3851.0 Safari/537.36');

  // Navigate the page to a URL
  let init_url = 'https://www.bestfightodds.com/archive'
  await page.setViewport({width: 1080, height: 1024});
  await page.goto(init_url,  {waitUntil: 'load', timeout: 35000});
  await sleep(1)
  let table_element = await page.$x('//*[@id="page-content"]/table')
  .find_elements_by_xpath(".//*")
  console.log(await table_element.children)
  // Set screen size

//   // Type into search box
//   await page.type('.search-box__input', 'automate beyond recorder');
// 
//   // Wait and click on first result
//   const searchResultSelector = '.search-box__link';
//   await page.waitForSelector(searchResultSelector);
//   await page.click(searchResultSelector);

//   // Locate the full title with a unique string
//   const textSelector = await page.waitForSelector(
//     'text/Customize and automate'
//   );
//   const fullTitle = await textSelector?.evaluate(el => el.textContent);

//   // Print the full title
//   console.log('The title of this blog post is "%s".', fullTitle);

  await browser.close();
})();
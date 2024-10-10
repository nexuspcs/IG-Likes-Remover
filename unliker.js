const puppeteer = require('puppeteer');
const path = require('path');

(async () => {
  // Path to your Chrome profile on macOS
  const userDataDir = path.join('/Users/jamescoates/Library/Application Support/Google/Chrome');

  // Launch Puppeteer with your existing Chrome profile
  const browser = await puppeteer.launch({
    headless: false,  // Show the browser
    args: [
      `--user-data-dir=${userDataDir}`,  // Use the existing session
    ],
  });

  const page = await browser.newPage();
  await page.goto('https://www.instagram.com/jamescoates_19/saved/');  // Change this to "liked" if needed

  // Wait for the page to load
  await new Promise(resolve => setTimeout(resolve, 5000));


  // Find and click all "Unlike" buttons
  const unlikeButtons = await page.$$(`article button[aria-label="Unlike"]`);

  let maxUnlikesPerHour = 2;  // Set the limit for unlikes per hour
  let unlikedCount = 0;

  for (const button of unlikeButtons) {
    if (unlikedCount >= maxUnlikesPerHour) {
      console.log(`Reached ${maxUnlikesPerHour} unlikes limit.`);
      break;
    }

    await button.click();  // Click the unlike button
    unlikedCount++;
    console.log(`Unliked ${unlikedCount} posts`);

    // Wait between actions to respect the limit (3600 seconds in an hour)
    await page.waitForTimeout(3600 / maxUnlikesPerHour * 1000);
  }

  await browser.close();  // Close the browser when done
})();

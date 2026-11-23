const puppeteer = require('puppeteer-core');
const path = require('path');
const fs = require('fs');

const CHROME_PATH = '/Applications/Google Chrome.app/Contents/MacOS/Google Chrome';
const SCREENSHOT_DIR = path.join(__dirname, '..', 'screenshots');

if (!fs.existsSync(SCREENSHOT_DIR)) {
  fs.mkdirSync(SCREENSHOT_DIR, { recursive: true });
}

async function run() {
  console.log('Launching headless Chrome from:', CHROME_PATH);
  const browser = await puppeteer.launch({
    executablePath: CHROME_PATH,
    headless: 'new',
    args: ['--no-sandbox', '--disable-setuid-sandbox', '--window-size=1440,900']
  });

  const page = await browser.newPage();
  await page.setViewport({ width: 1440, height: 900 });

  // 1. Initial Default Page
  console.log('Navigating to default TensorFlow Playground...');
  await page.goto('https://playground.tensorflow.org/', { waitUntil: 'networkidle2' });
  await new Promise(r => setTimeout(r, 2000));

  const defaultScreenshotPath = path.join(SCREENSHOT_DIR, 'tf_playground_default.png');
  await page.screenshot({ path: defaultScreenshotPath, fullPage: false });
  console.log('Saved default page screenshot to:', defaultScreenshotPath);

  // Inspect UI Elements
  const uiInspection = await page.evaluate(() => {
    const activations = Array.from(document.querySelectorAll('#activations option')).map(o => o.text);
    const regularizations = Array.from(document.querySelectorAll('#regularizations option')).map(o => o.text);
    const problemTypes = Array.from(document.querySelectorAll('#problem option')).map(o => o.text);
    const datasets = Array.from(document.querySelectorAll('.dataset')).map(d => d.getAttribute('data-dataset') || d.id || d.title || d.className);
    return { activations, regularizations, problemTypes, datasets };
  });
  console.log('UI Inspection Results:', JSON.stringify(uiInspection, null, 2));

  // 2. Experiment 1: Circle dataset
  console.log('\n--- Running Experiment 1: Circle Dataset ---');
  // Hash for circle, 2 layers (4,4), ReLU, lr=0.03, noise=15, ratio=50%
  const circleUrl = 'https://playground.tensorflow.org/#activation=relu&batchSize=10&dataset=circle&regDataset=reg-plane&learningRate=0.03&regularizationRate=0&noise=15&networkShape=4,4&seed=0.42&showTestData=false&discretize=false&percTrainData=50&x=true&y=true&xTimesY=false&xSquared=false&ySquared=false&cosX=false&sinX=false&cosY=false&sinY=false&collectStats=false&problem=classification&initZero=false&hideText=false';

  await page.goto(circleUrl, { waitUntil: 'networkidle2' });
  await new Promise(r => setTimeout(r, 2000));

  // Click play button
  console.log('Starting training for Circle...');
  await page.click('#play-pause-button');

  // Wait for epochs >= 250
  let circleMetrics = {};
  for (let i = 0; i < 40; i++) {
    await new Promise(r => setTimeout(r, 1000));
    circleMetrics = await page.evaluate(() => {
      const epoch = document.querySelector('#iter-number')?.innerText || '';
      const lossTest = document.querySelector('#loss-test')?.innerText || '';
      const lossTrain = document.querySelector('#loss-train')?.innerText || '';
      return { epoch: parseInt(epoch.replace(/,/g, ''), 10) || 0, lossTest, lossTrain };
    });
    console.log(`Epoch: ${circleMetrics.epoch}, Test Loss: ${circleMetrics.lossTest}, Train Loss: ${circleMetrics.lossTrain}`);
    if (circleMetrics.epoch >= 250) break;
  }

  // Pause training
  await page.click('#play-pause-button');
  await new Promise(r => setTimeout(r, 1000));

  const circleScreenshotPath = path.join(SCREENSHOT_DIR, 'tf_playground_circle_trained.png');
  await page.screenshot({ path: circleScreenshotPath, fullPage: false });
  console.log('Saved Circle trained screenshot to:', circleScreenshotPath);

  // 3. Experiment 2: Spiral dataset
  console.log('\n--- Running Experiment 2: Spiral Dataset ---');
  // Hash for spiral, 3 layers (6,4,2), Tanh, lr=0.03, noise=0, ratio=50%, all 7 features
  const spiralUrl = 'https://playground.tensorflow.org/#activation=tanh&batchSize=10&dataset=spiral&regDataset=reg-plane&learningRate=0.03&regularizationRate=0&noise=0&networkShape=6,4,2&seed=0.42&showTestData=false&discretize=false&percTrainData=50&x=true&y=true&xTimesY=true&xSquared=true&ySquared=true&cosX=false&sinX=true&cosY=false&sinY=true&collectStats=false&problem=classification&initZero=false&hideText=false';

  await page.goto(spiralUrl, { waitUntil: 'networkidle2' });
  await new Promise(r => setTimeout(r, 2000));

  console.log('Starting training for Spiral...');
  await page.click('#play-pause-button');

  let spiralMetrics = {};
  for (let i = 0; i < 60; i++) {
    await new Promise(r => setTimeout(r, 1000));
    spiralMetrics = await page.evaluate(() => {
      const epoch = document.querySelector('#iter-number')?.innerText || '';
      const lossTest = document.querySelector('#loss-test')?.innerText || '';
      const lossTrain = document.querySelector('#loss-train')?.innerText || '';
      return { epoch: parseInt(epoch.replace(/,/g, ''), 10) || 0, lossTest, lossTrain };
    });
    if (i % 5 === 0) {
      console.log(`Epoch: ${spiralMetrics.epoch}, Test Loss: ${spiralMetrics.lossTest}, Train Loss: ${spiralMetrics.lossTrain}`);
    }
    if (spiralMetrics.epoch >= 450) break;
  }

  await page.click('#play-pause-button');
  await new Promise(r => setTimeout(r, 1000));

  const spiralScreenshotPath = path.join(SCREENSHOT_DIR, 'tf_playground_spiral_trained.png');
  await page.screenshot({ path: spiralScreenshotPath, fullPage: false });
  console.log('Saved Spiral trained screenshot to:', spiralScreenshotPath);

  const results = {
    uiInspection,
    circleExperiment: circleMetrics,
    spiralExperiment: spiralMetrics
  };

  fs.writeFileSync(path.join(SCREENSHOT_DIR, 'playground_results.json'), JSON.stringify(results, null, 2));
  console.log('Saved playground_results.json');

  await browser.close();
  console.log('Simulation and screenshot capture finished successfully.');
}

run().catch(err => {
  console.error('Error during execution:', err);
  process.exit(1);
});

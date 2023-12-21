const path = require("path");
const { FFCreatorCenter, FFScene, FFImage, FFCreator } = require("ffcreator");

const bg1 = path.join(__dirname, "../assets/demo.jpg");
const cacheDir = path.join(__dirname, "../cache");

const creator = new FFCreator({
  cacheDir, // cache directory
  width: 474, // width of the video
  height: 711, // video height
  debug: false, // enable test mode
});

const scene1 = new FFScene();

const fbg1 = new FFImage({ path: bg1, x: 474/2, y: 711/2 });
scene1.addChild(fbg1);

scene1.setDuration(5);
creator.addChild(scene1);

creator.setOutput(path.join(__dirname, "../output/demo.mp4"));
creator.start();

creator.on("start", () => {
  console.log(`FFCreator start`);
});

creator.on("error", (e) => {
  console.log(`FFCreator error: ${e.error}`);
});

creator.on("progress", (e) => {
  console.log(`FFCreator progress: ${(e.percent * 100) >> 0}%`);
});

creator.on("complete", (e) => {
  console.log(`FFCreator completed: \n USAGE: ${e.useage} \n PATH: ${e.output}`);
  console.log(`\n --- You can press the s key or the w key to restart! --- \n`);
});

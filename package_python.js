const path = require("path");

const spawn = require("child_process").spawn,
  ls = spawn(
    "pyinstaller",
    [
      "-w",
      "--onefile",
      `--add-data web_app/app/templates${path.delimiter}templates`,
      `--add-data web_app/app/static${path.delimiter}static`,
      "--distpath dist-python",
      "web_app/run_app.py",
    ],
    {
      shell: true,
    }
  );

ls.stdout.on("data", function (data) {
  // stream output of build process
  console.log(data.toString());
});

ls.stderr.on("data", function (data) {
  console.log("Packaging error: " + data.toString());
});
ls.on("exit", function (code) {
  console.log("child process exited with code " + code.toString());
});

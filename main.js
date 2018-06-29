'use strict';

const electron = require('electron');
const app = electron.app;
const BrowserWindow = electron.BrowserWindow;
const path = require('path');

// Keep a global reference of the mainWindowdow object, if you don't, the mainWindowdow will
// be closed automatically when the JavaScript object is garbage collected.
var mainWindow = null;
var subpy = null;


// This method will be called when Electron has finished
// initialization and is ready to create browser mainWindow.
// Some APIs can only be used after this event occurs.
app.on('ready', function() {
	
	// spawn server
	subpy = require('child_process').spawn('python', [__dirname + '/web_app/run_app.py']);

  // Create the browser mainWindow
  mainWindow = new BrowserWindow({
    width: 800,
    height: 600,
    // transparent: true, // transparent header bar
    icon: __dirname + '/icon.png',
    // fullscreen: true,
    // opacity:0.8,
    // darkTheme: true,
    // frame: false,
    resizeable: true
  });

    // Load the index page
    mainWindow.loadURL('http://localhost:4040/');
  
	// Open the DevTools.
	//mainWindow.webContents.openDevTools();

	// Emitted when the mainWindow is closed.
	mainWindow.on('closed', function() {
    // Dereference the mainWindow object
    mainWindow = null;
  });
	
});

// disable menu
electron.app.on('browser-window-created',function(e,window) {
    window.setMenu(null);
});

// ------- app terminated

app.on('window-all-closed', function() {
	// quit app if windows are closed
  app.quit();
});

app.on('quit', function() {
	// kill the python server on exit
  subpy.kill('SIGINT');
});


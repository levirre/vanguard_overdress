//main.js
const electron = require('electron');
const url = require('url');
const path = require('path');


// This is like specific importing functions from a module in Python
// https://developer.mozilla.org/en-US/docs/Web/JavaScript/Guide/Modules
// from Cirle.py import GetArea

//import app and BrowserWindow modules from Electron
const {app, BrowserWindow, Menu } = electron;

let mainWindow;

// Listen for the app to be ready
app.on('ready',function(){
    //create new window
    mainWindow = new BrowserWindow({webPreferences:{
        nodeIntegration: true,
        contextIsolation: false
    }
    });
    //load html file into window
    mainWindow.loadURL(url.format({
        pathname: path.join(__dirname,'mainWindow.html'),
        protocol:'file',
        slashes: true
        // loads ./mainWindow.html
    }));
    //Remove Top menu bar
    mainWindow.setMenu(null);
    
    //This create the top bar header --File Edit Selection... etc
    //const mainMenu = Menu.buildFromTemplate(mainMenuTemplate);
    //Menu.setApplicationMenu(mainMenu);

    mainWindow.on('closed',function(){app.quit});

});






/*
const mainMenuTemplate = [{
    label:'File',
    submenu:[{label: 'Start New Game'},{label: 'Connect'},{label: 'Reconnect'},{label: 'Quit',click(){app.quit()}  }]
}]
*/


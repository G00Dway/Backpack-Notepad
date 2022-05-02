using System.Net;

WebClient webClient = new WebClient();
webClient.DownloadFile("https://raw.githubusercontent.com/G00Dway/Backpack-Notepad/main/Files/version.log", @"version.log");
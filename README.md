# Seal Counter App

This team project created during the WildHack2021. The app is purposed to analyze incoming photos and to search present seals for further counting and plotting.

### Developers
- Georgiy Andreev (Front-end developer) - [GitHub](https://github.com/andreevgeorge)
- Sergey Kitaev (Data scientist) - [GitHub](https://github.com/Sergey-Kit)
- Natalya Moskovka (Data scientist) - [Telegram](https://t.me/natchandes)

### Table of Contents

* [Roadmap](#roadmap)
* [Installation](#installation)
* [Running](#running)

## Roadmap

- [x]  Images are sorted by the days taken
- [x]  Processed folders are marked
- [x]  Data is stored into .csv file for history plotting
- [x]  Plot data .js file is automatically marked up 
- [x]  Data is visualised with the web interface
- [x]  Web interface is tied to the local commands
- [ ]  Trained NN is implemented into the pipeline
- [ ]  Paths are dynamically written or obtained via the web interface
- [ ]  (optional) App is wrapped into a single file (with a starting script)
- [ ]  (optional) App is optimised and dependency instllation process is automatised
- [ ]  All bugs are fixed

## Installation

The application uses both `Flask` and `Node.js` servers to run so check if these components are present. 

To install required JS packages run the following command in the `src` directory:
```bash
node i
```
## Running

To run the Flask server execute:

```python
python FlaskServer.py
```

To run the Node server execute:

```javascript
node start
```

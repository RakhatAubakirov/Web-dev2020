import React from 'react';
import { render } from "react-dom";

import Tabs from './tab/Tabs';




require('./styles.css');

function App() {
  return (
    <div class="wrapper">
      <h1>Tabs App//Web</h1>
      <Tabs>
        <div label="Active">
        
        </div>
        <div label="Default">
        </div>
        <div label="Default">
        </div>
      </Tabs>
    </div>
  );
}



const container = document.createElement('div');
document.body.appendChild(container);
render(<App />, container);


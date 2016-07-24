import React from 'react';
import {render} from 'react-dom';
import injectTapEventPlugin from 'react-tap-event-plugin';
import getMuiTheme from 'material-ui/styles/getMuiTheme';
import MuiThemeProvider from 'material-ui/styles/MuiThemeProvider';

import Board from './components/Board';

//Needed for onTouchTap
//Can go away when react 1.0 release
//Check this repo:
//https://github.com/zilverline/react-tap-event-plugin
injectTapEventPlugin();

class App extends React.Component {
  render () {
    return (
    	<MuiThemeProvider muiTheme={getMuiTheme()}>
    		<Board/>
		</MuiThemeProvider>
    );
  }
}

render(<App/>, document.getElementById('app'));
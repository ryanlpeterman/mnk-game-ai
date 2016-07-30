import React from 'react';
import RefreshIndicator from 'material-ui/RefreshIndicator';
import RaisedButton from 'material-ui/RaisedButton';
import Dialog from 'material-ui/Dialog';
import SelectField from 'material-ui/SelectField';
import MenuItem from 'material-ui/MenuItem';

import {Card, CardActions, CardHeader, CardMedia, CardTitle, CardText} from 'material-ui/Card';

import getMuiTheme from 'material-ui/styles/getMuiTheme';

let humanMark = 'X';
let computerMark = 'O';

let Cell = React.createClass({displayName: 'Cell',
	cellStyle: {
		height: 100,
		width: 100,
		outline: '1px solid',
		float: 'left'
	},

    handleClick : function () {

		if (this.props.mark === 'O' || this.props.mark === 'X') {
			alert('Invalid spot: already filled');
			return;
		}

		// update board with click
		this.props.updateBoard(this.props.idx);
    },

    render: function() {

	    let markerView;
	    // TODO change this representation to 1,0, -1
	    if (this.props.mark === 'X') {
	      markerView =(
	      <svg>
	        <line x1="10" y1="10" x2="90" y2="90" stroke="black" strokeWidth="2"/>
	        <line x1="10" y1="90" x2="90" y2="10" stroke="black" strokeWidth="2"/>
	      </svg>
	      )
	    }
	    else if (this.props.mark === 'O')
	      markerView = <svg><circle cx="50" cy="50" r="40" stroke="black" strokeWidth="2" fill="none"/> </svg>;


	    return (
	        <div style={this.cellStyle} onClick={this.handleClick}>
	          {markerView}
	        </div>
	    );
	}
});



let Board = React.createClass({displayName: 'Board',

	boardStyle: {
		width: 300,
		height: 300,

		position: 'absolute',
        left:0, right:0,
        top:0, bottom:0,
        margin:'auto'
	},

	cardStyle: {
		maxWidth: 800,

		width: '95%',
		height: '95%',

		position: 'absolute',
        left:0, right:0,
        top:0, bottom:0,
        margin:'auto'
	},

	selectStyle: {
		width: '40%',
		display: 'block'
	},

	childContextTypes:{
		muiTheme: React.PropTypes.object.isRequired,
	},

	getChildContext(){
		return {muiTheme: getMuiTheme()};
	},


	switchOpenState : function() {
		this.setState({open: !(this.state.open)});
	},

	switchDimensionDiagState : function() {
		this.setState({dim_open: !(this.state.dim_open)});
	},

	getInitialState: function() {
		return {
			board: [ ' ', ' ', ' '
					,' ', ' ', ' '
					,' ', ' ', ' '],
			loader: 'hide',
			open: false,
			dim_open: false,
			winner: undefined,
			m: 3,
			n: 3,
			k: 3}
	},

	updateBoard : function (idx) {

		// if board is loading, throw away click
		if (this.state.loader === 'loading' || this.state.winner !== undefined)
			return;
		var board = this.state.board;
		board[idx] = humanMark;
		this.setState({board: board, loader:'loading'});

		let int_board = this.state.board.map(
			function(char){
				if (char === 'O')
					return 1
				else if (char === 'X')
					return 0
				else
					return -1
			}
		)

		// make api call to get computer move
		var http = new XMLHttpRequest();
		var url = "http://127.0.0.1:5000/api/board"
		// var url = "https://tic-tac-toe-ai.herokuapp.com/api/board"

		http.open("POST", url);
		//Send the proper header information along with the request
		http.setRequestHeader("Content-type", "application/x-www-form-urlencoded");
		http.setRequestHeader("Access-Control-Allow-Origin", "*");
		var me = this;
		http.onreadystatechange = function() {//Call a function when the state changes.
		    if(http.readyState == 4 && http.status == 200) {
		        let res = JSON.parse(http.responseText);

		        // if valid move passed back then update views
		        if (res.row != -1 && res.col != -1) {
			        let board = me.state.board;
			        board[res.col + res.row*3] = computerMark;
			        me.setState({board: board, loader:'hide'});
		    	}

		    	// if winner was declared, declare it
		        if(res.winner != undefined){
		        	me.setState({board: me.state.board, loader:'hide', open: true, winner: res.winner});
		        }
		    }
		}

		http.send("board=" + JSON.stringify(int_board) + "&M=3&N=3&K=3");
	},

	render: function() {
		let me = this;

		let createCellFunc = function(tic, idx) {
			return (
				<Cell updateBoard={me.updateBoard} idx={idx} mark={tic}/>
			);
		};
		// prepare cells
		let cells = this.state.board.map(createCellFunc);

		let actions = [
	      <RaisedButton
	        label="Close"
	        secondary={true}
	        onTouchTap={this.switchOpenState}
	        style={{marginRight:20, marginBottom: 20}}
	      />
	    ];
	    let dimDiagActions = [
	    	<RaisedButton
	        label="Close"
	        secondary={true}
	        onTouchTap={this.switchDimensionDiagState}
	        style={{marginRight:20, marginBottom: 20}}
	      />
	    ];

	    let handleSelect = function(dimension) {
		  return function(event,index,value) {
		  	let state = {};
		  	state[dimension] = value;
			me.setState(state);
		  };
		 };

		let error = Math.max(this.state.m, this.state.n) < this.state.k;


		return (


			<Card style={this.cardStyle} zDepth={5}>
			    <CardTitle title="M,N,K Game AI Demo" subtitle="A generic AI" />

			    <div style={this.boardStyle}>
					{cells}
					<RefreshIndicator
						size={50}
						left={-25}
						top={300}
						style={{marginLeft:"50%", pointerEvents:"none"}}
						status={me.state.loader}
					/>
					<Dialog
			          title={this.state.winner}
			          actions={actions}
			          autoDetectWindowHeight={true}
			          modal={true}
			          open={me.state.open}
			          onRequestClose={me.switchOpenState}
			        >
			        </Dialog>
			        <Dialog
			          title={"Set board Dimensions"}
			          actions={dimDiagActions}
			          autoDetectWindowHeight={true}
			          modal={true}
			          open={me.state.dim_open}
			          onRequestClose={me.switchDimensionDiagState}
			        >
			        	<SelectField style={me.selectStyle} value={me.state.m} onChange={handleSelect('m')}>
				          <MenuItem value={3} primaryText="3" />
				          <MenuItem value={4} primaryText="4" />
				          <MenuItem value={5} primaryText="5" />
				          <MenuItem value={6} primaryText="6" />
				          <MenuItem value={7} primaryText="7" />
				        </SelectField>
      					<SelectField style={me.selectStyle} value={me.state.n} onChange={handleSelect('n')}>
				          <MenuItem value={3} primaryText="3" />
				          <MenuItem value={4} primaryText="4" />
				          <MenuItem value={5} primaryText="5" />
				          <MenuItem value={6} primaryText="6" />
				          <MenuItem value={7} primaryText="7" />
				        </SelectField>
				        <SelectField
				        	style={me.selectStyle}
				        	value={me.state.k}
				        	onChange={handleSelect('k')}
				        	errorText={error && 'K must be <= max(M,N)'}>

				          <MenuItem value={3} primaryText="3" />
				          <MenuItem value={4} primaryText="4" />
				          <MenuItem value={5} primaryText="5" />
				          <MenuItem value={6} primaryText="6" />
				          <MenuItem value={7} primaryText="7" />
				        </SelectField>
			        </Dialog>

				</div>

			    <CardText>
			      Tic Tac Toe is an m, n, k game where M=N=K=3.
			      With these parameters, the AI is unbeatable since
			      the AI can search the entire search space in less
			      than a second when alpha-beta pruning is implemented.

			      Note: since we are using a free Heroku instance to
			      the backend computation engine, the first move will take
			      a few seconds since the instance needs to "wake up".
			    </CardText>
			    <CardActions>
			      <RaisedButton label="Set Dimensions" primary={true} onTouchTap={me.switchDimensionDiagState}/>
			      <RaisedButton label="Reset Board" secondary={true} onTouchTap={function(){me.setState(me.getInitialState)}}/>
			    </CardActions>
			  </Card>

		);
	}
});

export default Board;
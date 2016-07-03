import React from 'react';

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
		margin: 'auto',
  		position: 'absolute',
  		top: 0, left: 0, bottom: 0, right: 0
	},

	getInitialState: function() {
		return {
			board: [ ' ', ' ', ' '
					,' ', ' ', ' '
					,' ', ' ', ' ']}
	},

	updateBoard : function (idx) {
		var board = this.state.board;
		board[idx] = humanMark;
		this.setState({board: board});

		console.log(board);

		// make api call to get computer move
		// TODO: Post request here
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
		return (
			<div style={this.boardStyle}>{cells}</div>
		);
	}
});

export default Board;
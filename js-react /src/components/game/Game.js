import React, { Component, useState } from 'react'
import Box from "../box/Box"
import "./game.css"

// export default class Game extends Component {
//     render
const board = [[], [], []];
function Game() {
    const [turn, setTurn] = useState('');

    function changeTurn(row, col) {

        setTurn(turn => turn === 'X' ? 'O' : 'X')
        board[row][col] = turn;
        chechForWin()
    }
    // for (let i = 0; i < board.length; i++) {
    //     for (let j = 0; j < board.length; j++) {
    //         if(turn==='X'){
    //             turn.style.color="red"
    //         }else{
    //             turn.style.color="green"
    //         }
            
    //     }
        
    // }
    function chechForWin() {
        // if(board[0][0]===board[0][1]&&board[0][0]===board[0][2]&&board[0][0]){
        //     alert("Winer is "+board[0][0])
        // }else if(board[1][0]===board[1][1]&&board[1][0]===board[1][2]&&board[1][0]){
        //     alert("We have a winer")
        // }else if(board[2][0]===board[2][1]&&board[2][0]===board[2][2]&&board[2][0]){
        //     alert("We have a winer")
        // }else if(board[0][0]===board[1][0]&&board[0][0]===board[2][0]&&board[0][0]){
        //     alert("We have a winer")
        // }else if(board[0][1]===board[1][1]&&board[0][1]===board[2][1]&&board[0][1]){
        //     alert("We have a winer")
        // }else if(board[0][2]===board[1][2]&&board[0][2]===board[2][2]&&board[0][2]){
        //     alert("We have a winer")
        // }else if(board[0][0]===board[1][1]&&board[0][0]===board[2][2]&&board[0][0]){
        //     alert("We have a winer")
        // }else if(board[0][2]===board[1][1]&&board[0][2]===board[2][0]&&board[0][2]){
        //     alert("We have a winer")

        // }else{
        //     console.log("just try to win")
        // }
        for (let i = 0; i < board.length; i++) {
            const row = board[i];
            // console.log(row)
            if (row[0] === row[1] && row[1] === row[2] && row[0]) {
                return alert("we have a winer: "+row[0])
            }
        }
        for (let i = 0; i < board.length; i++) {
            const col0 = board[0][i];
            const col1 = board[1][i];
            const col2 = board[2][i];
            if (col0 === col1 && col1 === col2 && col0) {
                return col0
            }
        }
        const right0 = board[0][0];
        const right1 = board[1][1];
        const right2 = board[2][2];
        if (right0 === right1 && right1 === right2 && right0) {
            return right0
        }
        const left0 = board[1][2];
        const left1 = board[1][1];
        const left2 = board[2][0];
        if (left0 === left1 && left1 === left2 && left0) {
            return left0
        }
    }


    return (
        <div id='game'>
            <div className='row'>
                <Box row={0} col={0} changeTurn={changeTurn} currentState={turn} />
                <Box row={0} col={1} changeTurn={changeTurn} currentState={turn} />
                <Box row={0} col={2} changeTurn={changeTurn} currentState={turn} />
            </div>
            <div className='row'>
                <Box row={1} col={0} changeTurn={changeTurn} currentState={turn} />
                <Box row={1} col={1} changeTurn={changeTurn} currentState={turn} />
                <Box row={1} col={2} changeTurn={changeTurn} currentState={turn} />
            </div>
            <div className='row'>
                <Box row={2} col={0} changeTurn={changeTurn} currentState={turn} />
                <Box row={2} col={1} changeTurn={changeTurn} currentState={turn} />
                <Box row={2} col={2} changeTurn={changeTurn} currentState={turn} />
            </div>
        </div>
    )
}
// }
export default Game;
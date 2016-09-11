import React, {Component} from 'react';

class App extends Component {

    renderNumbers() {
        var items = [1,2,3,4];

        return items.map(function(num) {
            return <p> 
                {num} 
            </p>
        })
    }

    render() {
        return <div>
            { this.renderNumbers() }
        </div>
    }

}

export default App;

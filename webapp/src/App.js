import React from 'react';
import './App.css';
import '@blueprintjs/core/lib/css/blueprint.css'
import Connection from './pages/Connection';
import MemberList from './pages/admin/MemberList';
import VotingList from './pages/admin/VotingList';

import {
  BrowserRouter as Router,
  Switch,
  Route,
  Link
} from "react-router-dom";

class App extends React.Component {
  async fetchResource() {
    let data = await fetch('http://localhost:8000/members/', {
      headers: {
        "Content-Type": "application/json",
        "Authorization": "Bearer eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJ0b2tlbl90eXBlIjoiYWNjZXNzIiwiZXhwIjoxNjAzNjQ1MTA1LCJqdGkiOiI3Zjg2YWQ1MzdhZTE0ZWMxYjdkYTk1YWJkMTFiNzc0MCIsInVzZXJfaWQiOjF9.uksREbLJ7cRfYe10Y4_P_lt_LaPh0fNqfEygmDceb0E",
      }
    });
    let json = await data.json();

    return json;
  }
  render() {
    return (
      <Router>
        <div>
          <nav>
            <ul>
              <li>
                <Link to="/connection">Connection</Link>
              </li>
              <li>
                <Link to="/member-list">Members</Link>
              </li>
              <li>
                <Link to="/voting-list">Voting</Link>
              </li>
            </ul>
          </nav>

          <Switch>
            <Route path="/connection">
              <Connection />
            </Route>
            <Route path="/member-list">
              <MemberList />
            </Route>
            <Route path="/voting-list">
              <VotingList />
            </Route>
          </Switch>
        </div>
      </Router>
    );
  }
}

export default App;

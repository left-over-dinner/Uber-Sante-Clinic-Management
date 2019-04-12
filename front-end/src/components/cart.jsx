import React, { Component } from 'react'
import {connect} from 'react-redux'
import {withRouter} from 'react-router-dom'
import {Loader, Tab} from 'semantic-ui-react'
import Appointment from './appointment'
import axios from "axios";

class Cart extends Component {
    constructor(props) {
        super(props);
        this.state = {
            appointments: [],
            loading:false,
            availabilities: [],
        }
    }

    componentDidMount() {
        if (this.props.userProfile) {
            this.setState({loading: true})
            this.getAvailabilities();
        }
    }


    render() {
         if(this.state.loading){
            return(
                <div className='registrationForm-Container'>
                    <div className='loader-container'>
                <Loader active  inline='centered' />
                    </div>
                </div>)
        }else {
             var today = " Appointments Cart";
             var nextweek = "Next Week" + " (" + 2 + ")";
             var thismonth = "This Month" + " (" + 3 + ")";
             var nextmonths = "Next Months" + " (" + 4 + ")";
             var pastevents = "Past Events" + " (" + 5 + ")";
             return (<div className='registrationForm-Container'>
                 <Tab className='appointment-tab' menu={{secondary: true, pointing: true}} panes={
                     [
                         {
                             menuItem: today,
                             render: () =>
                                 <Tab.Pane attached={false}>

                                 </Tab.Pane>
                         }
                     ]
                 }/>
             </div>)
         }
    }
}
function mapStateToProps(state){
    return {
        userProfile: state.Reducers.userProfile
    };

}
export default withRouter(connect(mapStateToProps)(Appointments));
import React, { Component } from 'react'
import {connect} from 'react-redux'
import {withRouter} from 'react-router-dom'
import {Tab} from 'semantic-ui-react'
import Appointment from './appointment'

class Dashboard extends Component {
    constructor(props) {
        super(props);
        this.state = {
        }
    }

    componentDidMount() {

    }
    render() {
        var today = "Today" + " (" + 1 + ")";
        var nextweek = "Next Week" + " (" + 2 + ")";
        var thismonth = "This Month" + " (" + 3 + ")";
        var nextmonths = "Next Months" + " (" + 4 + ")";
        var pastevents = "Past Events" + " (" + 5 + ")";
        return (<div className='registrationForm-Container'>
            <Tab menu={{secondary: true, pointing: true}} panes={
                [
                    {
                        menuItem: today,
                        render: () =>
                            <Tab.Pane attached={false}>
                                <Appointment/>
                            </Tab.Pane>
                    },
                    {
                        menuItem: nextweek,
                        render: () =>
                            <Tab.Pane attached={false}>
                                <Appointment/>
                            </Tab.Pane>
                    },
                    {
                        menuItem: thismonth,
                        render: () =>
                            <Tab.Pane attached={false}>
                                <Appointment/>
                            </Tab.Pane>
                    },
                    {
                        menuItem: nextmonths,
                        render: () =>
                            <Tab.Pane attached={false}>
                                <Appointment/>
                            </Tab.Pane>
                    },
                    {
                        menuItem: pastevents,
                        render: () =>
                            <Tab.Pane attached={false}>
                                <Appointment/>
                            </Tab.Pane>
                    },

                ]
            }/>
            <Appointment/>
        </div>)
    }
}
function mapStateToProps(state){
    return {
        userProfile: state.Reducers.userProfile
    };

}
export default withRouter(connect(mapStateToProps)(Dashboard));
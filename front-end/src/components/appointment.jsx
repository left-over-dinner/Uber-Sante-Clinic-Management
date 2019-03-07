import React, { Component } from 'react'
import {connect} from 'react-redux'
import {withRouter} from 'react-router-dom'
import {Icon} from 'semantic-ui-react'
import '../appointment.css'

class Appointment extends Component {
    constructor(props) {
        super(props);
        this.state = {
        }
    }

    componentDidMount() {

    }
    render() {
        return (
            <div className="listCal">
                <div className="cal-box">
                    <div className="cal-list">
                        <div className="cal-date">
                            <div className="cal-date-day">
                                31St Monday
                            </div>
                            <div className="cal-date-month">
                                January
                            </div>
                        </div>
                        <div className="cal-desc">
                            <div className="cal-title">
                                <span className="cal-title-des"> Xray control</span>
                                <span lassName="cal-title-time">  From 15:30 to 15:50 </span>
                            </div>
                        </div>
                        <div className="PMC-Delete-Edit-buttons">
                            <div className="note-author">
                                <Icon name="trash"/> Delete
                            </div>
                            <div className="note-author2">
                                <Icon name="edit"/> Edit
                            </div>
                        </div>
                    </div></div>
            </div>)
    }
}
function mapStateToProps(state){
    return {
        userProfile: state.Reducers.userProfile
    };

}
export default withRouter(connect(mapStateToProps)(Appointment));
import React, { Component } from 'react'
import {connect} from 'react-redux'
import {withRouter} from 'react-router-dom'
import UberLogo from '../images/uber-logo.jpg'
import {Icon} from 'semantic-ui-react'

class Topbar extends Component {
    constructor(props) {
        super(props);
        this.state = {
        }
    }

    componentDidMount() {

    }

    render() { //sdsd
        const { activeMenuItem } = this.props;
        return (
            <div className='main-container-topBar'>
            <div className='uberText'>UBER SANTÉ</div>

                <div className='topbar-text'>
                    <div>
                    {this.props.userProfile? 'Logged In As ('+this.props.userProfile.type+'): '+this.props.userProfile.email : ''}
                    </div>
                </div>
            </div>)
    }
}
function mapStateToProps(state){
    return {
        userProfile: state.Reducers.userProfile,
    };

}
export default withRouter(connect(mapStateToProps)(Topbar));
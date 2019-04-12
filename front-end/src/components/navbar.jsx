import React, { Component } from 'react'
import {connect} from 'react-redux'
import {withRouter} from 'react-router-dom'
import {Icon, Menu} from 'semantic-ui-react'

class Navbar extends Component {
    constructor(props) {
        super(props);
        this.state = {
        }
    }

    componentDidMount() {
        let props = this.props;
        setTimeout(function(){
        let path = window.location.href.split('/');
        console.log(path)
        if(path[path.length-1] === 'login'){
            props.dispatch({type: 'activeMenuItem', data: 'Login'});
        }else if(path[path.length-1] === 'register'){
            props.dispatch({type: 'activeMenuItem', data: 'Register'});

        }else if(path[path.length-1] === 'appointments'){
            props.dispatch({type: 'activeMenuItem', data: 'Appointments'});

        }else if(path[path.length-1] === 'availabilities'){
            props.dispatch({type: 'activeMenuItem', data: 'Availabilities'});

        }else if(path[path.length-1] === ''){
            props.dispatch({type: 'activeMenuItem', data: 'Home'});
        }else if(path[path.length-1] === 'cart'){
            props.dispatch({type: 'activeMenuItem', data: 'Cart'});
        }
         }, 1);

    }
    handleItemClick = (e, { name }) => this.props.dispatch({type: 'activeMenuItem', data: name});
    registeration =()=>{ this.props.history.push(`/register`);}
    login=()=>{this.props.history.push(`/login`) }
    home=()=>{this.props.history.push(`/`);}
    logout=()=> {
        this.props.history.push(`/`)
        localStorage.removeItem("jwtToken");
        this.props.dispatch({type: 'addUserProfile', data: ''});

    }
    appointments=()=>{this.props.history.push(`/appointments`)}
    availabilities=()=>{this.props.history.push(`/availabilities`)}
    cart=()=>{this.props.history.push(`/cart`)}

    render() {
        const { activeMenuItem } = this.props;
        console.log(this.props.userProfile)
        if(this.props.userProfile){
            return (
                <div className='navbar-container'>
                    <Menu pointing secondary vertical>
                        <Menu.Item
                            name='Home'
                            active={activeMenuItem === 'Home'}
                            fitted='Home'
                            onClick={(e,{name})=>{this.handleItemClick(e,{name});this.home();}}
                        >
                            Home
                        </Menu.Item>

                        <Menu.Item
                            name='Appointments'
                            active={activeMenuItem === 'Appointments'}
                            fitted='Appointments'
                            onClick={(e,{name})=>{this.handleItemClick(e,{name});this.appointments();}}
                        >
                            Appointments
                        </Menu.Item>
                        <Menu.Item
                            name='Availabilities'
                            active={activeMenuItem === 'Availabilities'}
                            fitted='Availabilities'
                            onClick={(e,{name})=>{this.handleItemClick(e,{name});this.availabilities();}}
                        >
                            Availabilities
                        </Menu.Item>
                        {this.props.userProfile.type === "Patient"?
                        <Menu.Item
                            name='Cart'
                            active={activeMenuItem === 'Cart'}
                            fitted='Cart'
                            onClick={(e,{name})=>{this.handleItemClick(e,{name});this.cart();}}
                        >

                        </Menu.Item>: null}

                        <Menu.Item
                            name='Logout'
                            active={activeMenuItem === 'Logout'}
                            fitted='Logout'
                            onClick={(e,{name})=>{this.handleItemClick(e,{name});this.logout();}}
                        >
                            Logout
                        </Menu.Item>


                    </Menu></div>)

        }else{
            return (
                <div className='navbar-container'>
                    <Menu pointing secondary vertical>
                        <Menu.Item
                            name='Home'
                            active={activeMenuItem === 'Home'}
                            fitted
                            onClick={(e,{name})=>{this.handleItemClick(e,{name});this.home();}}
                        >
                            Home
                        </Menu.Item>

                        <Menu.Item
                            name='Register'
                            active={activeMenuItem === 'Register'}
                            fitted='Register'
                            onClick={(e, { name })=>{ this.handleItemClick(e, { name });this.registeration();}}
                        >
                            Register
                        </Menu.Item>

                        <Menu.Item
                            name='Login'
                            active={activeMenuItem === 'Login'}
                            fitted='Login'
                            onClick={(e,{name})=>{this.handleItemClick(e,{name});this.login();}}
                        >
                            Login
                        </Menu.Item>
                    </Menu></div>)

        }
    }
}
function mapStateToProps(state){
    return {
        userProfile: state.Reducers.userProfile,
        activeMenuItem: state.Reducers.activeMenuItem
    };

}
export default withRouter(connect(mapStateToProps)(Navbar));
const initialState = {
    userProfile: '',
    activeMenuItem:'Home',
}
export default (state = initialState, action) => {
    switch (action.type) {
        case 'addUserProfile':
            return { ...state, userProfile: action.data };
        case 'activeMenuItem':
            return { ...state, activeMenuItem: action.data };
        default:
            return state;
    }
};
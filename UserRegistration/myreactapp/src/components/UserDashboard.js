
import React from 'react';
import UserProfile from './UserProfile';
import EditProfileForm from './EditProfileForm';
import AllUserProfiles from './AllUserProfiles';
import RegistrationForm from './RegistrationForm';

const UserDashboard = () => {
    return (
        <div>
            <h2>Your Profile</h2>
            <UserProfile />
            
            <h3>Edit Profile</h3>
            <EditProfileForm />

            <h3>All User Profiles</h3>
            <AllUserProfiles />

            <h3>Register a New User</h3>
            <RegistrationForm />
        </div>
    );
};

export default UserDashboard;

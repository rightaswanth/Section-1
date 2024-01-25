
import React, { useState } from 'react';
import axios from 'axios';

const RegistrationForm = () => {
    const [formData, setFormData] = useState({
        username: '',
        email: '',
        password: '',
        bio: '',  
    });

    const handleChange = (e) => {
        setFormData({ ...formData, [e.target.name]: e.target.value });
    };

    const handleSubmit = async (e) => {
        e.preventDefault();

        try {
            await axios.post('http://localhost:8000/api/register/', formData);
            console.log('User registered successfully');
        }catch (error) {
        
            console.error('Error registering user:', error);
        }
    };

return(
        <form onSubmit={handleSubmit}>
            <label>Username:</label>
            <input type="text" name="username" onChange={handleChange} value={formData.username} required />

            <label>Email:</label>
            <input type="email" name="email" onChange={handleChange} value={formData.email} required />

            <label>Password:</label>
            <input type="password" name="password" onChange={handleChange} value={formData.password} required />

            {/* Add additional registration fields as needed */}
            <label>Bio:</label>
            <textarea name="bio" onChange={handleChange} value={formData.bio} />

            <button type="submit">Register</button>
        </form>
    );
};

export default RegistrationForm;

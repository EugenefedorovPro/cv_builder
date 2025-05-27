import React from 'react';
import './Header.styles.css';

interface HeaderProps {
    name?: string;
    phone?: string;
    email?: string;
    linkedin?: string;
    github?: string;
    country?: string;
    city?: string;
    district?: string;
    photo?: string;
    created_at?: string;
    updated_at?: string;
}

const HeaderCV: React.FC<HeaderProps> = ({
                                             name = 'Your Name',
                                             phone = 'Phone Number',
                                             email = 'email@example.com',
                                             linkedin,
                                             github,
                                             country = 'Country',
                                             city = 'City',
                                             district,
                                             photo,
                                         }) => {
    return (
        <header className="cv-header">
            <div className="photo-container">
                {photo ? (
                    <img src={photo} alt="Profile" className="profile-photo" />
                ) : (
                    <div className="photo-placeholder" aria-label="No profile photo">
                        <span>Photo</span>
                    </div>
                )}
            </div>
            <div className="header-content">
                <h1 className="name">{name}</h1>
                <div className="contact-info">
                    <p>{phone}</p>
                    <p>{email}</p>
                    {linkedin && (
                        <p>
                            <a href={linkedin} target="_blank" rel="noopener noreferrer">
                                LinkedIn
                            </a>
                        </p>
                    )}
                    {github && (
                        <p>
                            <a href={github} target="_blank" rel="noopener noreferrer">
                                GitHub
                            </a>
                        </p>
                    )}
                </div>
                {(country || city || district) && (
                    <p className="location">
                        {district && `${district}, `}
                        {city && `${city}, `}
                        {country}
                    </p>
                )}
            </div>
        </header>
    );
};

export default HeaderCV;

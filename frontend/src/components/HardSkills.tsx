import React from 'react';
import './HardSkills.styles.css';

interface HardSkill {
    hard_skill_text: string;
}

interface HardSkillsCVProps {
    hardSkills?: HardSkill[];
}

const HardSkillsCV: React.FC<HardSkillsCVProps> = ({hardSkills}) => {
    const skillsToRender = hardSkills && hardSkills.length > 0
        ? hardSkills
        : [
            {hard_skill_text: 'JavaScript'},
            {hard_skill_text: 'React'},
            {hard_skill_text: 'TypeScript'},
            {hard_skill_text: 'Django'},
        ];

    return (
        <header className="cv-header">
            <div className="hard-skills-container">
                <h2 className="cv-title">Hard Skills</h2>
                <ul className="hard-skills-list">
                    {skillsToRender.map((skill, index) => (
                        <li key={index} className="skill-item">
                            {skill.hard_skill_text}
                        </li>
                    ))}
                </ul>
            </div>
        </header>
    );
};

export default HardSkillsCV;

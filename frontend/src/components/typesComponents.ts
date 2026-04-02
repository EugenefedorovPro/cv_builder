export interface HeaderBlockNamesInterface {
  education_name: string;
}

export interface EducationItemInterface {
  id: number;
  institution: string;
  start_date: string;
  end_date: string;
  degree_title: string;
}

export interface EducationBlockInterface {
  education: EducationItemInterface[];
  block_names: HeaderBlockNamesInterface;
}

export interface HeaderBlockNamesInterface {
  experience_name: string;
  company_title: string;
  exp_period_title: string;
  position_title: string;
  achievements_title: string;
}

export interface ExperienceItemInterface {
  id: number;
  company: string;
  position: string;
  start_date: string;
  end_date?: string;
  achievements: string;
}

export interface ExperienceBlockInterface {
  experience: ExperienceItemInterface[];
  block_names: HeaderBlockNamesInterface;
}

// HardSkill
export interface HardSkillsBlockNameObject {
  hard_skills_name?: string | null;
}

export interface HardSkillsItemInterface {
  id: number;
  category: string;
  hard_skill_text: string;
}

export interface HardSkillsInterface {
  block_names: HardSkillsBlockNameObject;
  hard_skills: HardSkillsItemInterface[];
}

// Header
export interface PhotoInterface {
  photo_url: string;
}

export interface HeaderBlockNamesInterface {
  github_title?: string;
  linkedin_title?: string;
  country_title?: string;
  city_title?: string;
  district_title?: string;
}

export interface HeaderInterface {
  id: number;
  first_name: string;
  second_name: string;
  phone: string;
  email: string;
  city?: string | null;
  country?: string | null;
  district?: string | null;
  github?: string | null;
  linkedin?: string | null;
  photo?: PhotoInterface | null;
}

export type HeaderBlockType = {
  header: HeaderInterface;
  block_names: HeaderBlockNamesInterface;
};

export interface BlockNameInterface {
  interest_name: string;
}

export interface InterestItemInterface {
  id: number;
  interest_text: string;
}

export interface InterestBlockInterface {
  interests: InterestItemInterface[];
  block_names: BlockNameInterface;
}
export interface HeaderBlockNamesInterface {
  block_names: string;
}

export interface ManifestItemInterface {
  id: number;
  manifest_text: string;
}

export interface ManifestBlockInterface {
  manifest: ManifestItemInterface;
  block_names: HeaderBlockNamesInterface;
}
export interface BlockNameInterface {
  natural_lang_name: string;
}

export interface NaturalLangItemInterface {
  id: number;
  natural_lang: string;
  level: string;
}

export interface NaturalLangBlockInterface {
  natural_langs: NaturalLangItemInterface[];
  block_names: BlockNameInterface;
}

export interface BlockNameInterface {
  natural_lang_name: string;
}

export interface NaturalLangItemInterface {
  id: number;
  natural_lang: string;
  level: string;
}

export interface NaturalLangBlockInterface {
  natural_langs: NaturalLangItemInterface[];
  block_names: BlockNameInterface;
}

export interface ProjectItemInterface {
  id: number;
  project_name: string;
  project_text: string;
  web_url: string | null;
  git_url: string | null;
}

export interface BlockNameInterface {
  block_names: string;
}

export interface ProjectsBlockInterface {
  projects: ProjectItemInterface[];
  block_names: BlockNameInterface;
}
export interface BlockNameInterface {
  soft_skills_name: string;
}

export interface SoftSkillItemInterface {
  id: number;
  soft_skill_text: string;
}

export interface SoftSkillsBlockInterface {
  soft_skills: SoftSkillItemInterface[];
  block_names: BlockNameInterface;
}

const API_BASE = process.env.NODE_ENV && process.env.NODE_ENV === "development" ? "http://localhost:8000" : "http://localhost:80";

const BACKEND_URL: string = `${API_BASE}/api`;
const CLOUDINARY_BASE_URL: string = "https://res.cloudinary.com/shayon-cloud/image/upload/v1691683509";
const MAX_SIGNIN_COOKIE_AGE: number = 60 * 60 * 24; // One day


// console.log(process.env.NUXT_BACKEND_URL, process.env.NODE_ENV, process.env.BACKEND_API, process.env.NUXT_ENV_EXAMPLE);

export { BACKEND_URL, CLOUDINARY_BASE_URL, MAX_SIGNIN_COOKIE_AGE };

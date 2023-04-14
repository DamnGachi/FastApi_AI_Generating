import Gallery from "./pages/Gallery"
import Admin from "./pages/Admin"
import Auth from "./pages/Auth"
import Photo from "./pages/PhotoPage"
import { ADMIN_ROUTE, GALLERY_ROUTE, LOGIN_ROUTE, PHOTO_ROUTE, REGISTRATION_ROUTE } from "./utils/consts"

export const authRoutes = [
    {
        path: ADMIN_ROUTE,
        Component: Admin
    },
    {
        path: GALLERY_ROUTE,
        Component: Gallery
    }
]
export const publicRoutes = [
    {
        path: GALLERY_ROUTE,
        Component: Gallery
    },
    {
        path: LOGIN_ROUTE,
        Component: Auth
    },
    {
        path: REGISTRATION_ROUTE,
        Component: Auth
    },
    {
        path: PHOTO_ROUTE,
        Component: Photo
    }
]

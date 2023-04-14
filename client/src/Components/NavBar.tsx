import React, { useContext } from 'react';
import { Context } from '../index';
import Navbar from 'react-bootstrap/esm/Navbar';
import Nav from 'react-bootstrap/esm/Nav';
import { NavLink } from 'react-router-dom';
import { ADMIN_ROUTE, LOGIN_ROUTE, GALLERY_ROUTE } from '../utils/consts';
import { Button, Container } from 'react-bootstrap';
import { observer } from "mobx-react-lite";
import { useNavigate } from 'react-router-dom';


const NavBar = observer(() => {
    let { user } = useContext(Context)
    let navigate = useNavigate()

    let logOut = () => {
        user.setUser({})
        user.setIsAuth(false)
    }

    return (
        <Navbar bg="dark" variant="dark">
            <Container>
                <NavLink style={{ color: 'white' }} to={GALLERY_ROUTE}>Gallery</NavLink>
                {user._isAuth ?
                    <Nav className="ml-auto" style={{ color: 'white' }}>
                        <Button
                            variant={"outline-light"}
                            onClick={() => navigate(ADMIN_ROUTE)}
                        >
                            Админ панель
                        </Button>
                        <Button
                            variant={"outline-light"}
                            onClick={() => logOut()}
                            className="ml-2"
                        >
                            Выйти
                        </Button>
                    </Nav>
                    :
                    <Nav className="ml-auto" style={{ color: 'white' }}>
                        <Button variant={"outline-light"} onClick={() => navigate(LOGIN_ROUTE)}>Authorize</Button>
                    </Nav>
                }
            </Container>
        </Navbar>

    );
});

export default NavBar;

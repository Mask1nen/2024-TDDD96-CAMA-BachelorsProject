import React from 'react';
import AppBar from '@mui/material/AppBar';
import Box from '@mui/material/Box';
import Toolbar from '@mui/material/Toolbar';
import IconButton from '@mui/material/IconButton';
import Typography from '@mui/material/Typography';
import Menu from '@mui/material/Menu';
import MenuIcon from '@mui/icons-material/Menu';
import Container from '@mui/material/Container';
import Avatar from '@mui/material/Avatar';
import Button from '@mui/material/Button';
import Tooltip from '@mui/material/Tooltip';
import MenuItem from '@mui/material/MenuItem';
import AdbIcon from '@mui/icons-material/Adb';
import { Link } from "react-router-dom";
import { logout, useAuth } from '../hooks/useAuth';
import multiLanguage from "../components/multiLanguage";
import changeLanguageBotton from "../../src/assets/navBarText/changeLanguageButton.json";
import {Context} from "../../src/App";
import { useContext } from 'react';


const pages = ['Home', 'Subjects', 'Apps', 'Database'];


function Navbar() {
  const [anchorElNav, setAnchorElNav] = React.useState<null | HTMLElement>(null);
  const [anchorElUser, setAnchorElUser] = React.useState<null | HTMLElement>(null);

  const [isSWE, setIsSWE] = useContext(Context);

  {/*
  const [isSWE2, setIsSWE2] = useState(false);
  languageVariable.value = isSWE2;
*/}

  const handleOpenNavMenu = (event: React.MouseEvent<HTMLElement>) => {
    setAnchorElNav(event.currentTarget);
  };
  const handleOpenUserMenu = (event: React.MouseEvent<HTMLElement>) => {
    setAnchorElUser(event.currentTarget);
  };

  const handleCloseNavMenu = () => {
    setAnchorElNav(null);
  };

  const handleCloseUserMenu = () => {
    setAnchorElUser(null);
  };

  const handleLogout = () => {
    logout();
    window.location.href = "/Home";
  };

  //Remove line below and uncomment the line below that to enable login redirect
  let redirect_uri = "Upload"
  //let redirect_uri = "Login"

  const [isLoggedIn, session] = useAuth();
  if (isLoggedIn) {
    redirect_uri = "Upload";
  }

  return (
    <AppBar position="sticky" color="default">
      <Container maxWidth="xl">
        <Toolbar disableGutters>
          <AdbIcon sx={{ display: { xs: 'none', md: 'flex' }, mr: 1 }} />
          <Typography
            variant="h6"
            noWrap
            component="a"
            href="#app-bar-with-responsive-menu"
            sx={{
              mr: 2,
              display: { xs: 'none', md: 'flex' },
              fontFamily: 'monospace',
              fontWeight: 700,
              letterSpacing: '.3rem',
              color: 'inherit',
              textDecoration: 'none',
            }}
          >
            LOGO
          </Typography>

          <Box sx={{ flexGrow: 1, display: { xs: 'flex', md: 'none' } }}>
            <IconButton
              size="large"
              aria-label="account of current user"
              aria-controls="menu-appbar"
              aria-haspopup="true"
              onClick={handleOpenNavMenu}
              color="inherit"
            >
              <MenuIcon />
            </IconButton>
            <Menu
              id="menu-appbar"
              anchorEl={anchorElNav}
              anchorOrigin={{
                vertical: 'bottom',
                horizontal: 'left',
              }}
              keepMounted
              transformOrigin={{
                vertical: 'top',
                horizontal: 'left',
              }}
              open={Boolean(anchorElNav)}
              onClose={handleCloseNavMenu}
              sx={{
                display: { xs: 'block', md: 'none' },
              }}
            >
              {pages.map((page) => (
                <MenuItem key={page} onClick={handleCloseNavMenu}>
                  <Typography textAlign="center">{page}</Typography>
                </MenuItem>
              ))}
            </Menu>
          </Box>
          <AdbIcon sx={{ display: { xs: 'flex', md: 'none' }, mr: 1 }} />
          <Typography
            variant="h5"
            noWrap
            component="a"
            href="#app-bar-with-responsive-menu"
            sx={{
              mr: 2,
              display: { xs: 'flex', md: 'none' },
              flexGrow: 1,
              fontFamily: 'monospace',
              fontWeight: 700,
              letterSpacing: '.3rem',
              color: 'inherit',
              textDecoration: 'none',
            }}
          >
            LOGO
          </Typography>
          <Box sx={{ flexGrow: 1, display: { xs: 'none', md: 'flex' } }}>
            {pages.map((page) => (
              <Link 
                to={page}>
                <Button
                  key={page}
                  onClick={handleCloseNavMenu}
                  sx={{  color: 'black', display: 'block' }}
                  >
                  {page}
                </Button>
              </Link>
            ))}
          </Box>


          <Box sx={{ flexGrow: 0, display:"flex"}}>
            <Button size="small" variant="contained" color="primary" sx={{ height: "31px", margin: "0 auto", mr:3}} 
            onClick={() => setIsSWE(!isSWE)} > {multiLanguage(!isSWE, changeLanguageBotton)}</Button>
              
              <Link to={redirect_uri}>
                <Button size="small"
                  key="addstudy"
                  variant="contained"
                  color="primary"
                  sx={{mr:3}}

                >
                  Add Study
                </Button>
              </Link>
            
            {isLoggedIn && <Tooltip title="Open settings">
              <IconButton onClick={handleOpenUserMenu} sx={{ p: 0 }}>
                <Avatar sx={{ width: "40px", height: "40px", margin: "0 auto" }} />
              </IconButton>
            </Tooltip>}

            {/**
             * Temporary login button, can be removed or kept
             * depending on the design choice.
             */}
            {!isLoggedIn && <Link to="Login">
              <Button size="small"
                  key="login"
                  variant="contained"
                  color="primary"
                  sx={{mr:3}}
                >
                  Login
                </Button>
                </Link>
            }

            <Menu
              sx={{ mt: '45px' }}
              id="menu-appbar"
              anchorEl={anchorElUser}
              anchorOrigin={{
                vertical: 'top',
                horizontal: 'right',
              }}
              keepMounted
              transformOrigin={{
                vertical: 'top',
                horizontal: 'right',
              }}
              open={Boolean(anchorElUser)}
              onClose={handleCloseUserMenu}
            >
                <MenuItem key="Profile" onClick={handleCloseUserMenu}>
                  <Link to="Profile">
                    <Typography textAlign="center">Profile</Typography>
                  </Link>
                </MenuItem>
                <MenuItem key="Logout" onClick={handleLogout}>
                  <Typography textAlign="center">Logout</Typography>
                </MenuItem>
            </Menu>
          </Box>
        </Toolbar>
      </Container>
    </AppBar>
  );
}
export default Navbar;
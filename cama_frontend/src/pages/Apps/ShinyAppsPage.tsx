import { useState } from 'react';
import { Box, Tab, Tabs, Typography, CircularProgress, Alert } from '@mui/material';

const ShinyAppDisplay = () => {
    const [selectedTab, setSelectedTab] = useState(-1); // Start with no tab selected
    const [isLoading, setIsLoading] = useState(false);

    const handleChange = (event, newValue) => {
        setSelectedTab(newValue);
        setIsLoading(true); // Set loading true when tab changes
    };

    const handleLoad = () => {
        setIsLoading(false); // Set loading false when iframe loads
    };

    const appUrls = [
        'http://wanda.lnu.se:3838/bayesian_meta/',
        'http://wanda.lnu.se:3838/data_validation/',
        'http://wanda.lnu.se:3838/frequentist_meta/'
    ];

    const appTitles = [
        "Bayesian Meta Analysis",
        "Data Validation",
        "Frequentist Meta Analysis"
    ];

    return (
        <Box sx={{ width: '100%', padding: 3 }}>
            <Typography variant="h4" sx={{ marginBottom: 2 }}>
                Shiny Apps Dashboard
            </Typography>
            <Typography variant="subtitle1" sx={{ marginBottom: 2 }}>
                Click on the app you want to use, please give the models some time to load.
            </Typography>
            <Alert severity="info" sx={{ marginBottom: 2 }}>
                Please ensure you are connected to the VPN to access these applications.
            </Alert>
            <Tabs value={selectedTab} onChange={handleChange} aria-label="Shiny Apps Tabs">
                {appTitles.map((title, index) => (
                    <Tab label={title} key={index} />
                ))}
            </Tabs>
            {selectedTab !== -1 && (
                <Box sx={{ border: 1, borderColor: 'divider', mt: 2, minHeight: '500px', position: 'relative' }}>
                    {isLoading && (
                        <CircularProgress
                            size={50}
                            sx={{
                                position: 'absolute',
                                top: '50%',
                                left: '50%',
                                transform: 'translate(-50%, -50%)'
                            }}
                        />
                    )}
                    <iframe
                        src={appUrls[selectedTab]}
                        title="Shiny App"
                        style={{ width: '100%', height: '700px', border: 'none', display: isLoading ? 'none' : 'block' }}
                        onLoad={handleLoad}
                        allowFullScreen
                    />
                </Box>
            )}
        </Box>
    );
};


export default ShinyAppDisplay;
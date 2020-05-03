from distutils.core import setup

setup(
    name='deepillusion',         
    packages=['deepillusion'],   
    version='0.0.2',      
    license='MIT',        
    description='Adversarial Machine Learning ToolBox',   
    author='Metehan Cekic',                   
    author_email='metehancekic@ucsb.edu',     
    url='https://github.com/metehancekic/deep-illusion.git',
    download_url='https://github.com/metehancekic/deep-illusion/archive/v_001.tar.gz',    
    keywords=['Adversarial', 'Attack', 'Pytorch'],   
    install_requires=[           
        'tqdm',
        'numpy',
        ],
    classifiers=[
        # Chose either "3 - Alpha", "4 - Beta" or "5 - Production/Stable" as the current state of your package
        'Development Status :: 3 - Alpha',
        'Intended Audience :: Developers',      # Define that your audience are developers
        'Topic :: Software Development :: Build Tools',
        'License :: OSI Approved :: MIT License',   # Again, pick a license
        'Programming Language :: Python :: 3',  # Specify which pyhton versions that you want to support
        'Programming Language :: Python :: 3.4',
        'Programming Language :: Python :: 3.5',
        'Programming Language :: Python :: 3.6',
        ],
)

# scifitropes

## Exploring Science Fiction works and tropes with data from TVTropes.org.

These datasets are a jumping off point for exploring 1) trope density (see "Tropes Count" column) among science fiction works and 2) trope frequency across different subsets of tropes, and 3) each trope's associated works.

The driving idea is that by quantifying different science fiction images of the future, we can begin to explore different relationships between images of the future and society, for example:

* Analyzing the tropes perpetuated in the highest grossing science fiction movies on the list by combining the films list with box office data from another source.
* Adding metadata about year of original release in order to explore trope frequencies over time and detect trends in both narrative and speculative fiction tropes across decades, media, etc.
* Works across different media with high trope density but low influence versus low trope density but high influence (cult classics or seminal works)
* Analyze differences in speculative trope frequencies between Anime and Western Animation in order to explore different cultural perspectives of the future.

## Initial Release

***Note: TVTropes is licensed under a Creative Commons Attribution-NonCommercial-ShareAlike 3.0 Unported License, so please respect said license when creating any derivative works.***

These top level csv files are each sorted in descending order by the # of tropes listed with that work. The list of works are based on the works listed on the subpages of the [Science Fiction](https://tvtropes.org/pmwiki/pmwiki.php/Main/ScienceFiction) page on TVTropes.org

The trope lists are derived from the [Futuristic Tech Index](https://tvtropes.org/pmwiki/pmwiki.php/Main/FuturisticTechIndex).
 
I am working on building sets of data from TVTropes.org about science fiction specifically in addition to lists that allow futurists and strategic foresight practitioners to probe science fiction works for tropes related to subgenres, STEEP categories, religion, and narrative more broadly in order to assist their work. But obviously anyone is free to use and help refine the data!

I am not a coder or a data scientist really, so these have been generated by using pseudocode--or really poor descriptions--of the tasks I'd like to accomplish using OpenAI's GPT-4 model on ChatGPT which then returned python scripts I could copy and paste to run from the command line on UNIX-based systems. From there it was a trial and error process of refining code, refining outputs, etc. on ChatGPT. This is just a project I've always wanted to do but didn't really have the time to explore until I could use AI as a copilot to work through my lack of coding skills, so I hope it's useful!

The examples folder currently contains the python script that combined and deduped the URLs across the lists in order to generate the 'mainscifiworkstropesdb.csv' file. 

The plan is for the data in this repository to remain focused strictly on getting the most accurate and comprehensive list of science fiction works and their tropes across all media types to support:

* Academic research
* Critical analysis of science fiction works
* Finding gaps in TVTropes.org's current science fiction lists for works, tropes, creators, and more in order to contribute back to the extremely valuable resource that this is based on.

## Known Issues

I will add to the Issues in the repo as well, but just to flag some issues that I know need to be resolved sooner rather than later:

* Deduping trope lists across works in order to confirm more accurate trope counts per work.
* You will notice some large media properties have no tropes lists--this is due to either differences in how the html is structured for that property's page or if the trope lists exist at a different url (ex. "Red Dwarf"). I am working on seeing if there is a generalizable approach to gathering those or if they need to be run through individually. They are easy to find yourself in the lists since they are sorted in descending order--just jump down to the bottom.
* Franchises are also missing if they exist on a '/Franchise/' containing URL.
* Some urls are "http://tvtropes.org" and others are "https://www.tvtropes.org"; if someone helps clean this up by changing all instances to "https://tvtropes.org" I'd be very grateful.


## Additional Plans in the Short Term

* ASAP: Add a folder of curated lists of tropes - namely the speculative fiction and futuristic tech lists.
* TV Series episodes (aka Recaps) have not been explored. Eager to do this and likely add to the 'trope density' of more series.
* ~~Plan to add 'laconic' summaries for all trope lists so trope meanings are easier to understand and accessible to a wider audience. Initially planned to include the laconic summaries for works but would prefer to avoid spoilers if people use it to discover new works they wanna check out.~~ Done for all future tech trope sub-lists. Will show up in main list on next update to that file.
* Address works with missing lists
* Address missing "Franchises"
* Figuring out how to add data from other datasets or APIs to the base files to expand utility.
* Adding more examples of how to analyze the datasets.




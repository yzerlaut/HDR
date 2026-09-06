# Role of NDNF+ Interneurons in Cortical Processing

%%beginFigure%%
![](../Figures/ndnf-raw.svg)
**| Activity of NDNF+ interneurons in mouse V1 during behaviour and visual stimulation.**
**(a)** Schematic of the recording rig.
**(b)** Field of View of the 2-photon recording in layer 1.
**(c)** From top to bottom. Raster plot view of the $\Delta$F/F over all ROIs. Temporal variations of $\Delta$F/F traces in four interneurons (green). Pupil trace (red). Gaze movement (orange, evaluated as the position of the centre of the ellipse fitted to the pupil). Whisking activity (purple, evaluated from the motion energy of the camera recording in the whisker pad area). Locomotion activity (blue).  
Unpublished data from Van Velze, Gonzalez, Rebola & Zerlaut.
%%endFigure%%

Neuron-derived neurotrophic factor (NDNF) has emerged, over roughly the past decade, as a selective genetic marker for a distinct population of GABAergic interneurons concentrated in neocortical layer 1 (L1), largely corresponding to neurogliaform-type cells and distinguishable from the other major L1 interneuron subtypes identified through single-cell transcriptomic and morphological profiling ([Schuman et al., 2018](Schuman2018.pdf)).
This localisation is functionally significant: layer 1 is the principal cortical target of long-range, top-down projections (from higher-order cortical areas, thalamus, and neuromodulatory centres), placing NDNF interneurons in a privileged position to integrate contextual and behaviourally relevant information arriving from outside the local sensory circuit.

The first detailed functional characterisation of this population showed that NDNF interneurons in auditory cortex provide widespread inhibition, both onto other interneurons in L1 and lower layers and, critically, directly onto the distal dendrites of pyramidal neurons, via a connection with a pronounced, slow GABA-B receptor-mediated component ([Abs et al., 2018](Abs2018.pdf)).
This prolonged dendritic inhibition was shown to directly gate the initiation of dendritic spikes in pyramidal neurons, and, strikingly, to be itself plastic: NDNF-interneuron sensory responses became potentiated following associative (fear) learning, in direct proportion to the strength of the resulting memory. 

Beyond associative learning, NDNF/L1 interneurons have also been implicated in the state-dependent regulation of dendritic inhibition more broadly, with their action on pyramidal dendrites varying across periods of quiet wakefulness and active behavioural engagement in sensory cortex ([Cohen-Kashi Malina et al., 2021](CohenKashiMalina2021.pdf), see also our own recordings in [Fig.](../Figures/ndnf-raw.svg)).
Recent work has extended this picture, characterising NDNF interneurons as specialised "master regulators" coordinating top-down influence over cortical circuits across multiple levels of organisation ([Hartung et al., 2024](Hartung2024.pdf)), and providing a first theoretical, circuit-level account of how NDNF-mediated inhibition is specifically organised across cortical layers ([Naumann et al., 2025](Naumann2025.pdf)).


%%beginFigure%%
![](../Figures/ndnf-evoked.svg)
**| Visually-evoked activity of NDNF+ interneurons for different types of visual stimuli.** 
**(a)** Set of different stimuli used for visual stimulation.
**(b)** Example responses (trial-averaged) in a single neuron for the different stimulus types.
**(c)** Summary statistics for the visually-evoked responses. 
Top. Fraction of significant positive responses in all recorded NDNF+ interneurons. 
Bottom. Average $\Delta$F/F response in the post-stimulus window for each stimulus (the different bars for some stimuli represent their different realisations, e.g. 4 directions for the drifting gratings, 5 different natural images, etc...). 
Note the positive responses for some stimuli (e.g. natural images, static patch) and the negative responses for some others (e.g. the drifting gratings).  
Unpublished data from Gonzalez, Van Velze, Rebola & Zerlaut.
%%endFigure%%

Despite this progress, the functional role of NDNF interneurons remains, in many respects, still enigmatic. 
In particular, while their anatomical position and dendrite-targeting connectivity make them well suited to modulate how sensory information is represented in cortical circuits, direct evidence for such a role remains scarce: most existing work has focused on their engagement during associative learning ([Abs et al., 2018](Abs2018.pdf)) or their state-dependent recruitment ([Cohen-Kashi Malina et al., 2021](CohenKashiMalina2021.pdf)), rather than on their consequences for the structure of sensory representations themselves. 
How NDNF interneurons shape stimulus tuning, response reliability, or population-level coding in sensory cortex (as opposed to simply gating dendritic excitability at specific behavioural or learning-related moments) remains an open question.

To address this question, we recorded the responses of NDNF+ interneurons to a range of visual stimuli: static patches, natural images, drifting gratings, moving dots, and random dots.
These stimuli engage a wide range of integration mechanisms in the visual system, including mostly feedforward drive, long-range lateral interactions, feedback from higher-order cortical areas, and feedback from subcortical structures, among others.

These recordings revealed a diverse set of responses (see [Fig.](../Figures/ndnf-evoked.svg)), with some stimuli driving strong net recruitment of NDNF+ interneurons (static patches, natural images), while others appeared to suppress their activity (drifting gratings), thus pointing to a potential stimulus-dependent disinhibitory mechanism.

Our current work aims to understand the impact of this diversity of responses on the pyramidal neurons NDNF+ interneurons innervate, using optogenetic inhibition of NDNF-INs.
This work will reveal the role of NDNF+ interneurons in shaping visual representations in the mouse visual cortex.



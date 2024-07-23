import 'package:camera/camera.dart';
import 'package:flutter/material.dart';
import 'package:frontend/src/components/widgets/cameradisplay.dart';
import 'package:frontend/src/core/services/imageservice.dart' as imageservice;

class HomePage extends StatefulWidget {
  final CameraDescription camera;

  const HomePage({super.key, required this.camera});

  @override
  State<HomePage> createState() => _HomePageState();
}

class _HomePageState extends State<HomePage> {
  late CameraController _controller;
  late Future<void> _initializeControllerFuture;

  @override
  void initState() {
    super.initState();
    _controller = CameraController(widget.camera, ResolutionPreset.medium);
    _initializeControllerFuture = _controller.initialize();
  }

  @override
  Widget build(BuildContext context) {
    return Scaffold(
      appBar: AppBar(
        title: const Center(child: Text("MathPics")),
        backgroundColor: Theme.of(context).colorScheme.inversePrimary,
      ),
      body: Center(
        child: Column(
          children: [
            CameraDisplay(controller: _controller, initializeControllerFuture: _initializeControllerFuture,),
            const Text("Hello!"),
            ElevatedButton(onPressed: () async {
              XFile image = await _controller.takePicture();
              imageservice.makePrediction(image).then((res) {
                print(res);
              });
            }, child: const Text('Take a picture!')),
          ],
        ),
      ),
    );
  }
}